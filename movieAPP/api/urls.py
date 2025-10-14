from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.db import router

from movieAPP.api.views import ReviewCreate, ReviewDetail, ReviewList, StreamPlatformAV, StreamPlatformDetailAV, WatchListVS


router = DefaultRouter()
router.register(r'list', WatchListVS, basename='list')

urlpatterns = [
    path('', include(router.urls)),

    path('list/<int:pk>/review-create/',
         ReviewCreate.as_view(), name="review-create"),
    path('list/<int:pk>/reviews/', ReviewList.as_view(), name='movie-detail'),
    path('list/rviews/<int:pk>/', ReviewDetail.as_view(), name='movie-detail'),

    path('streams/', StreamPlatformAV.as_view(), name="streams"),
    path('streams/<int:pk>', StreamPlatformDetailAV.as_view(),
         name="streamplatform-detail"),

    path('reviews/', ReviewList.as_view(), name="reviews"),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name="review-detail")
]
