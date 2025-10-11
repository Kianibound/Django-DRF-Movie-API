from django.urls import path

from movieAPP.api.views import ReviewDetail, ReviewList, StreamPlatformAV, StreamPlatformDetailAV, WatchListAV, WatchListDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movies-list'),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('list/<int:pk>/reviews', ReviewDetail.as_view(), name='movie-detail'),
    path('streams/', StreamPlatformAV.as_view(), name="streams"),
    path('streams/<int:pk>', StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    path('streams/<int:pk>/reviews', StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    path('reviews/', ReviewList.as_view(), name="reviews"),
    path('reviews/<int:pk>', ReviewDetail.as_view(), name="review-detail")
]
