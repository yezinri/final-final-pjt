from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review

# 11.19 DB 받아오기 위해 추가
import requests
import json

# 11.20 영화 알고리즘 추천
import random
import pprint

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def review_list(request, movie_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, movie_id=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    username = request.user.username
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user, username=username)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_likes(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        is_like = False
    else:
        review.like_users.add(request.user)
        is_like = True

    context = {
        'is_like': is_like,
    }
    return Response(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_like = False
    else:
        movie.like_users.add(request.user)
        is_like = True

    context = {
        'is_like': is_like,
    }
    return Response(context)


# 회원가입 시 랜덤영화 보여주기
@api_view(['GET'])
# @permission_classes([IsAuthenticated]) # 왜 이거 설정하면 에러뜰까
def random_movies(request):
    top_movies_json = open('movies/fixtures/movies.json', encoding='utf-8')    # topratedmovies DB 10000개
    top_movies = json.load(top_movies_json)                                 # 리스트 안에 있는 딕셔너리 형태

    genres_json = open('movies/fixtures/genres.json', encoding='utf-8')            # 장르 DB
    genres = json.load(genres_json)      


    original_genres = []                                        # 전체 장르 id를 담을 리스트
    for genre in genres:
        original_genres.append(genre['fields']['genre_id'])     # for문 돌려서 장르 id를 리스트에 담아줌
    original_genres.remove(99)                                  # 원래 장르 19개에서 99번 장르인 '다큐멘터리'는 제외했음. (DB에 장르 99번 영화가 없기 때문)
    original_genres.sort()                                      # 오름차순으로 정렬
    # print(original_genres)


    random_top_movies = random.sample(top_movies, 35)           # 일단 랜덤으로 35개의 영화를 가져옴
    selected_genres = []                                        # 랜덤으로 가져온 35개의 영화의 장르를 넣어줄 리스트
    for random_top_movie in random_top_movies:
        genre_ids = random_top_movie['fields'].get('genre_ids') 
        for genre_id in genre_ids:
            selected_genres.append(genre_id)                    # 영화들의 장르 아이디들을 리스트에 담아줌

    selected_genres = sorted(list(set(selected_genres)))        # set로 중복 제거하고 오름차순 정렬
    # print(selected_genres)

    if selected_genres != original_genres:                      
        not_contained_genres = original_genres                  # 현재 없는 장르
        for selected_genre in selected_genres:
            not_contained_genres.remove(selected_genre)     
        # print(not_contained_genres)

        for not_contained_genre in not_contained_genres:
            genre_movies = []
            for top_movie in top_movies:
                if not_contained_genre in top_movie['fields']['genre_ids']:
                    genre_movies.append(top_movie)

            # print(genre_movies)
            while True:
                random_genre_movie = random.sample(genre_movies, 1)
                if random_genre_movie not in random_top_movies:
                    random_top_movies.append(random.sample(genre_movies, 1))
                    # print(len(random_top_movies))
                    break
                

        while len(random_top_movies) < 40:
            while True:
                random_top_movie = random.sample(top_movies, 1)
                if random_top_movie not in random_top_movies:
                    random_top_movies.append(random.sample(genre_movies, 1))
                    break
                
        # print(len(random_top_movies), 'end!!')
        # pprint(random_top_movies)


    else:
        # print('oh')
        while len(random_top_movies) < 40:
            while True:
                random_top_movies.append(random.sample(top_movies, 1))
                if random_top_movie not in random_top_movies:
                    random_top_movies.append(random.sample(top_movies, 1))
                    break

        # print(len(random_top_movies), 'end!!')
        # pprint(random_top_movies)
    print(len(random_top_movies))
    context = {
        'random_top_movies': random_top_movies,
    }
    return Response(context)



# 영화 DB API로 받아오는 함수 (11.19 민혁 추가)
@api_view(['GET'])
def get_db(request):
    for i in range(1, 527):
        URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-kr&page=' + str(i)

        print(i)  # 그냥 출력 확인용
        response = requests.get(URL).json()
        movies = response['results']

        for movie in movies:
            added_movie = Movie(       
                adult = movie['adult'],
                movie_id = movie['id'],   
                title = movie['title'],
                genre_ids = movie['genre_ids'],  
                overview = movie['overview'],
                release_date = movie['release_date'],
                popularity = movie['popularity'],
                vote_average = movie['vote_average'],
                poster_path = movie['poster_path'],
                backdrop_path = movie['backdrop_path'],
            )
            added_movie.save()

            context = {
                 added_movie,
             }

    return Response(context) 