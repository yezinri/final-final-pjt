from rest_framework import serializers
from .models import Movie, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie

        fields = ('title', 'poster_path', 'id',)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie

        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review

        fields = '__all__'
        read_only_fields = ('movie', 'user', 'like_users',)