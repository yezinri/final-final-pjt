from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review

from accounts.models import User # 민혁 추가 11.21
from django.contrib.auth import get_user_model # 민혁 추가


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
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    if request.method == 'GET':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
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
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id=movie_pk)
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
    movie = Movie.objects.get(movie_id=movie_pk)

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

@api_view(['GET'])
def search(request, searchword):
    search_movies = Movie.objects.filter(title__contains=searchword)
    serializer = MovieSerializer(search_movies, many=True)
    return Response(serializer.data)


# 회원가입 시 랜덤영화 보여주기
@api_view(['GET'])
# @permission_classes([IsAuthenticated]) # 왜 이거 설정하면 에러뜰까
def random_movies(request):
    top_movies_json = open('movies/fixtures/all_movies.json', encoding='utf-8')    # topratedmovies DB 10000개
    top_movies = json.load(top_movies_json)                                 # 리스트 안에 있는 딕셔너리 형태

    genres_json = open('movies/fixtures/genres.json', encoding='utf-8')            # 장르 DB
    genres = json.load(genres_json)      


    original_genres = []                                        # 전체 장르 id를 담을 리스트
    for genre in genres:
        original_genres.append(genre['fields']['genre_id'])     # for문 돌려서 장르 id를 리스트에 담아줌
    original_genres.remove(99)                                  # 원래 장르 19개에서 99번 장르인 '다큐멘터리'는 제외했음. (DB에 장르 99번 영화가 없기 때문)
    original_genres.sort()                                      # 오름차순으로 정렬
    # print(original_genres)

    selected_top_movies = []
    for top_movie in top_movies:
        if top_movie['fields']['popularity'] >= 100:
            selected_top_movies.append(top_movie)

    print(len(selected_top_movies))
            



    random_top_movies = random.sample(selected_top_movies, 42)           # 일단 랜덤으로 42개의 영화를 가져옴
    selected_genres = []                                        # 랜덤으로 가져온 42개의 영화의 장르를 넣어줄 리스트
    for random_top_movie in random_top_movies:
        genre_ids = random_top_movie['fields']['genre_ids']
        for genre_id in genre_ids:
            selected_genres.append(genre_id)                    # 영화들의 장르 아이디들을 리스트에 담아줌

    selected_genres = sorted(list(set(selected_genres)))        # set로 중복 제거하고 오름차순 정렬
    # print(selected_genres)

    if selected_genres != original_genres:                      
        not_contained_genres = original_genres                  # 현재 없는 장르
        for selected_genre in selected_genres:
            not_contained_genres.remove(selected_genre)     
        print(not_contained_genres)

        for not_contained_genre in not_contained_genres:
            genre_movies = []
            for top_movie in top_movies:
                if not_contained_genre in top_movie['fields']['genre_ids']:
                    genre_movies.append(top_movie)

            # print(genre_movies)
            while True:
                random_genre_movie = random.sample(genre_movies, 1)[0]
                if random_genre_movie not in random_top_movies:
                    random_top_movies.append(random_genre_movie)
                    # print(len(random_top_movies))
                    break
                
        print(len(random_top_movies))
        while len(random_top_movies) < 48:
            while True:
                random_top_movie = random.sample(top_movies, 1)[0]
                if random_top_movie not in random_top_movies:
                    random_top_movies.append(random_top_movie)
                    break
                
        # print(len(random_top_movies), 'end!!')
        # pprint(random_top_movies)


    else:
        # print('oh')
        while len(random_top_movies) < 48:
            while True:
                random_top_movie = random.sample(top_movies, 1)[0]
                if random_top_movie not in random_top_movies:
                    random_top_movies.append(random_top_movie)
                    break

        # print(len(random_top_movies), 'end!!')
    #     pprint(random_top_movies[0])
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

# 영화 추천 함수
@api_view(['GET'])
def recommend(request, username):
    person = get_object_or_404(get_user_model(), username=username)

    liked_movies_id_list = []
    for like_movies in person.like_movies.all():                # 요게 핵심..
        liked_movies_id_list.append(like_movies.movie_id)
        # print(like_movies.movie_id)
    # print(liked_movies_id_list)

    recommended_movies = []
    how_many = []                       # 추천된 영화 id 목록
    for liked_movies_id in liked_movies_id_list:
        for i in range(1, 3):
            URL = 'https://api.themoviedb.org/3/movie/' + str(liked_movies_id) + '/recommendations?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-KR&page=' + str(i)
            response = requests.get(URL).json()
            movies = response['results']

            # pprint(movies)
    
            for movie in movies:
                recommended_movies.append(movie)
                how_many.append([movie['id'], movie['popularity']])
                # print(how_many) 


    how_many2 = {}  # 미쳤다..       영화 추천된 cnt랑 popularity 동시에 넣어줌
    for el in how_many:
        if el[0] in how_many2:
            how_many2[el[0]] = [how_many2[el[0]][0] + 1, el[1]]    
            pass
        else:
            how_many2[el[0]] = [1, el[1]]
        # print(how_many2)

    # print(how_many2)



    # <병진햄의 알고리즘 조언!!!> - 감사합니다~
    # how_many2 = []
    # for idx, id in enumerate(how_many):
    #     for otheridx, cnt, otherid, info in enumerate(how_many2):
    #         if id == otherid:
    #             how_many2[otheridx][0] += 1
    #             break
    #     else:
    #         how_many2.append([1, id, info])

    # how_many2.sort()
    # # [cnt, id, {영화정보}]


    how_many2 = list(how_many2.items())
    how_many2.sort(key=lambda x: x[1], reverse=True)
    # print(how_many2)
    how_many2 = how_many2[0:20]


    how_many2 = random.sample(how_many2, 12)
    how_many2.sort(key=lambda x: x[1], reverse=True)
    # print(how_many2)


    recommended_ids = []
    for id in how_many2:
        recommended_ids.append(id[0])

    # print(len(recommended_movies))

    # 리스트 안에 있는 중복된 딕셔너리 제거하는 방법
    not_redundant_movies = list({recommended_movie['id']: recommended_movie for recommended_movie in recommended_movies}.values())
    # print(len(not_redundant_movies))

    # # recommended_movies = list(set(recommended_movies))
    final_movies = []
    for id in recommended_ids:
        for not_redundant_movie in not_redundant_movies:
            if not_redundant_movie['id'] == id:
                final_movies.append(not_redundant_movie)

    # print(len(final_movies))
            

    context = {
        'final_movies': final_movies
    }
    return Response(context)

# 영화 detail 페이지에 보여줄 추천/관련 영화 리스트 (11.23 민혁추가)
@api_view(['GET'])
def similar_movies(request, movie_pk):

    similar_movies = []
    for i in range(1, 3):
        URL = 'https://api.themoviedb.org/3/movie/' + str(movie_pk) + '/recommendations?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-KR&page=' + str(i)
        response = requests.get(URL).json()
        movies = response['results']
        for movie in movies:
            if movie  not in similar_movies:    # 페이지 url에서 가져오면서 간혹 중복되는 경우가 있음
                similar_movies.append(movie)

    # print(similar_movies)
    # print(len(similar_movies))

    random_similar_movies = random.sample(similar_movies, 12)
    # print(random_similar_movies)
    # print(len(random_similar_movies))
    
    context = {
        'random_similar_movies': random_similar_movies
    }
    return Response(context)


# 최신영화 추천 및 DB 저장 알고리즘
@api_view(['GET'])
def latest_movies(request):

    top_movies_json = open('movies/fixtures/all_movies.json', encoding='utf-8')    # topratedmovies DB 10000개
    top_movies = json.load(top_movies_json)  
    
    # movies = Movie.objects.raw('select movie_id from ')
    latest_movies = []
    for i in range(1, 4):
        URL = 'https://api.themoviedb.org/3/movie/now_playing?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-KR&page=' + str(i)

        # print(i)  # 그냥 출력 확인용
        response = requests.get(URL).json()

        # print(response)
        movies = response['results']

        # DB에 저장하는 과정
        # top_movie_ids = []
        # for idx, top_movie in enumerate(top_movies):
        #     top_movie_ids.append(top_movie['fields']['movie_id'])
        #     print(idx)

        for movie in movies:
            latest_movies.append(movie)
        
        random_latest_movies = random.sample(latest_movies, 12)   

        for random_latest_movie in random_latest_movies:
            # if random_latest_movie['id'] not in top_movie_ids:
            added_movie = Movie(       
                adult = random_latest_movie['adult'],
                movie_id = random_latest_movie['id'],   
                title = random_latest_movie['title'],
                genre_ids = random_latest_movie['genre_ids'],  
                overview = random_latest_movie['overview'],
                release_date = random_latest_movie['release_date'],
                popularity = random_latest_movie['popularity'],   
                vote_average = random_latest_movie['vote_average'],
                poster_path = random_latest_movie['poster_path'],
                backdrop_path = random_latest_movie['backdrop_path'],
            )
            added_movie.save()
            # print(added_movie)
            # print(idx, '아래')

        # axios에 보내주는 과정

    context = {
        'random_latest_movies': random_latest_movies
    }

    return Response(context) 


from datetime import date

@api_view(['GET'])
def today_movie(request):

    today = int(date.today().strftime('%Y%m%d'))    # 오늘 날짜를 str형태로 받아와서 int로 바꾸어줌 e.g) 20221124

    movies = get_list_or_404(Movie)                 # 영화 전체 DB 가져옴

    cnt = 1                                         # 영화 id와 정확히 일치하지 않을 수 있으니 그냥 7번 기회를 줌
    while cnt < 8:
        coincidence = 0                             # 영화 id와 today 숫자가 일치하는가?
        for movie in movies:
            if movie.movie_id == today:
                coincidence += 1
                break                               # 일치하면 for문 종료       
        
        if coincidence > 0:                         # 일치하면 while문 종료
            break

        today = (today // 10) + 96                  # 일치하지 않으면 그냥 10으로나는 몫에 96 더해줌 (그냥 우리가 96년생이어서임)
        cnt += 1

    if cnt > 8:                                     # 기회 7번 날리면
        today = 274                                 # 그냥 손민혁이 제일 좋아하는 영화인 양들의 침묵 보는거다.. (한니발 존멋)

    # print(cnt)
    # print(coincidence)
    # print(today)

    today_movie = get_object_or_404(Movie, movie_id=today)
 
    serializer = MovieSerializer(today_movie)

    return Response(serializer.data)