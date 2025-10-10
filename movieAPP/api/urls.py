from django.urls import path

from movieAPP.api.views import StreamPlatformAV, StreamPlatformDetailAV, WatchListAV, WatchListDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movies-list'),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('streams/', StreamPlatformAV.as_view(), name="streams"),
    path('streams/<int:pk>', StreamPlatformDetailAV.as_view(), name="strems-detail")
]
