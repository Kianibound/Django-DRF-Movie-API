from django.forms import CharField
from rest_framework import serializers
from movieAPP.models import Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name', read_only=True)
    platform_id = serializers.PrimaryKeyRelatedField(
        source='platform', queryset=StreamPlatform.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
