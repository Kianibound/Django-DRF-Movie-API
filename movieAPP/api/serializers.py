from django.forms import ValidationError, fields
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from movieAPP.models import StreamPlatform, WatchList


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['id']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Name and Description Should Be Different")
    #     return data

    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is Too Short!")
    #     return value


# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name is Too Short!")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Name and Description Should Be Different")
#         return data

    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is Too Short!")
    #     return value
