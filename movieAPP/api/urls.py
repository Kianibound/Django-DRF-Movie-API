from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.db import router

from movieAPP.api.views import MovieListGV, ReviewCreate, ReviewDetail, ReviewList, StreamPlatformVS, WatchListAV, WatchListDetailAV


router = DefaultRouter()
router.register(r'streams', StreamPlatformVS, basename='streams')

urlpatterns = [
    path('', include(router.urls)),

    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('list2/', MovieListGV.as_view(), name="movie-list2"),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name="movie-detail"),

    path('list/<int:pk>/review-create/',
         ReviewCreate.as_view(), name="review-create"),
    path('list/<int:pk>/reviews/', ReviewList.as_view(), name='movie-reviews'),
    path('list/rviews/<int:pk>/', ReviewDetail.as_view(),
         name='movie-review-detail'),

    path('reviews/', ReviewList.as_view(), name="reviews"),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name="review-detail")
]
