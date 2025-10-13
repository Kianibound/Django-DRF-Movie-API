from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from django.shortcuts import get_object_or_404
from movieAPP.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
# from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import  status, generics
from movieAPP.models import Review, StreamPlatform, WatchList
from movieAPP.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchListSerializer
from rest_framework import viewsets


class WatchListVS(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class StreamPlatformAV(APIView):
    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            streams, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error: Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AdminOrReadOnly]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        # Check if this user already posted a review for this watchlist
        review_queryset = Review.objects.filter(
            watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("User has already posted a review")

        # Save both the watchlist and the review_user on the review instance
        serializer.save(watchlist=watchlist, review_user=review_user)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#         queryset = Review.objects.all()
#         serializer_class = ReviewSerializer

#         def get(self, request, *args, **kwargs):
#             return self.retrieve(request, *args, **kwargs)


# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         print(movies)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error: Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ReviewVS(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


# class WatchListVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = WatchList.objects.all()
#         serializer_class = WatchListSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         queryset = WatchList.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = WatchListSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = WatchListSerializer( data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class WatchListAV(APIView):
#     def get(self, request):
#         movies = WatchList.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = WatchListSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class WatchListDetailAV(APIView):

#     def get(self, request, pk):
#         try:
#             movie = WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             return Response({'Error: Not Found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         movie = WatchList.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
