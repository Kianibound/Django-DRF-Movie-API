from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.renderers import JSONRenderer
from movieAPP.api.pagination import WatchListLOPagination
from movieAPP.api.throttling import ReviewListThrottle, WatchListThrottle
from movieAPP.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics, status
from movieAPP.models import Review, StreamPlatform, WatchList
from movieAPP.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchListSerializer
from rest_framework import viewsets


class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [WatchListThrottle]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetailAV(APIView):
    permission_classes = [IsReviewUserOrReadOnly]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error: Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewListThrottle]
    filter_backends = [SearchFilter]
    filterset_fields = ['review_user__username', 'active']


class MovieListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['avg_rating']
    pagination_class = WatchListLOPagination
    renderer_classes = [JSONRenderer]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("User has already posted a review")

        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (
                watchlist.avg_rating + serializer.validated_data['rating']) / 2

        serializer.save(watchlist=watchlist, review_user=review_user)

        agg = Review.objects.filter(watchlist=watchlist).aggregate(
            avg_rating=Avg('rating'))
        watchlist.number_of_ratings = Review.objects.filter(
            watchlist=watchlist).count()
        watchlist.avg_rating = agg['avg_rating'] or 0
        watchlist.save()
