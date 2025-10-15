from rest_framework.throttling import UserRateThrottle


class WatchListThrottle(UserRateThrottle):
    scope = 'watchlist'


class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'
