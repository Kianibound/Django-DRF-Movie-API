from django.urls import path

from movieAPP.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movies-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
]
