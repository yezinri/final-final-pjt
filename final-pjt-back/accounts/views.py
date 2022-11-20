from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import User

import requests
import json
import pprint


# Create your views here.
@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'username': person.username,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
    }
    return Response(context)

# 영화 추천 함수
@api_view(['GET', 'POST'])
def recommend(request, username):

    person = get_object_or_404(get_user_model(), username=username)

    liked_movies_id_list = []
    for like_movies in person.like_movies.all():                # 요게 핵심..
        liked_movies_id_list.append(like_movies.movie_id)
        # print(like_movies.movie_id)
    print(liked_movies_id_list)

    how_many = []                       # 추천된 영화 id 목록
    for liked_movies_id in liked_movies_id_list:
        for i in range(1, 3):
            URL = 'https://api.themoviedb.org/3/movie/' + str(liked_movies_id) + '/recommendations?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-KR&page=' + str(i)
            response = requests.get(URL).json()
            movies = response['results']

            # pprint(movies)

 
            for movie in movies:
                how_many.append(movie['id'])
    
    print(how_many)
# 여기서부터 어떻게 가장 많은 순서대로 정렬을 하고 해당 영화 상위 5~10개를 가져올지 생각해보자.
         

    context = {
        'how_many': how_many
    }
    return Response(context)



    # context = {
    #     'like_movies': person.like_movies
    # }

    # return Response(context)