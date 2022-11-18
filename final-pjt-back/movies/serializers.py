from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie

        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review

        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username', 'like_users',)