from django.urls import path

from movieAPP.api.views import movie_details, movies_list

urlpatterns = [
    path('list/', movies_list, name='movies-list'),
    path('<int:pk>/', movie_details, name='movie-detail'),
]
