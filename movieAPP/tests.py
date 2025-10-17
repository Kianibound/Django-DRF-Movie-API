from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import response, status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from movieAPP.models import Review, StreamPlatform, WatchList
from movieAPP.api import serializers


class WatchlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.stream = StreamPlatform.objects.create(
            name='Netflix', about='Streaming', website='https://netflix.com')
        self.watchlist = WatchList.objects.create(
            platform=self.stream, title='Test Movie', description='Test Description', active=True)

    def test_watchlist_create(self):
        data = {
            'platform': self.stream.id,
            'title': 'Test Movie',
            'description': 'Test Description',
            'active': True
        }

        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_detail(self):
        response = self.client.get(
            reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WatchList.objects.get().title, 'Test Movie')
        self.assertEqual(WatchList.objects.count(), 1)
