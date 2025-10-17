from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from movieAPP.models import Review, StreamPlatform, WatchList


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


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.stream = StreamPlatform.objects.create(
            name='Netflix', about='Streaming', website='https://netflix.com')
        self.watchlist = WatchList.objects.create(
            platform=self.stream, title='Test Movie', description='Test Description', active=True)
        self.watchlist2 = WatchList.objects.create(
            platform=self.stream, title='Test Movie', description='Test Description', active=True)
        self.review = Review.objects.create(
            watchlist=self.watchlist2,
            review_user=self.user,
            rating=5,
            content='Test Review',
            active=True
        )

    def test_review_create(self):
        data = {
            'review_user': self.user.id,
            'rating': 5,
            'content': 'Test Description',
            'watchlist': self.watchlist.id,
            'active': True
        }

        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauthorized(self):
        self.client.force_authenticate(user=None)
        data = {
            'review_user': self.user.id,
            'rating': 5,
            'content': 'Test Description',
            'watchlist': self.watchlist.id,
            'active': True
        }
        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            'review_user': self.user.id,
            'rating': 4,
            'content': 'Test Description',
            'watchlist': self.watchlist2.id,
            'active': False
        }
        response = self.client.put(
            reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.get().rating, 4)

    def test_review_list(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_detail(self):
        response = self.client.get(
            reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
