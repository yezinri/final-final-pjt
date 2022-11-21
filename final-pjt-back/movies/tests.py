# from django.test import TestCase

# 11.19 추가 - 알고리즘 데이터 추출 목적
import json                         # JSON 파일 가져올 목적
from pprint import pprint

import random                       # 랜덤 영화 추출 목적

# Create your tests here.


top_movies_json = open('fixtures/all_movies.json', encoding='utf-8')    # topratedmovies DB 10000개
top_movies = json.load(top_movies_json)                                 # 리스트 안에 있는 딕셔너리 형태

genres_json = open('fixtures/genres.json', encoding='utf-8')            # 장르 DB
genres = json.load(genres_json)      



original_genres = []                                        # 전체 장르 id를 담을 리스트
for genre in genres:
    original_genres.append(genre['fields']['genre_id'])     # for문 돌려서 장르 id를 리스트에 담아줌
original_genres.remove(99)                                  # 원래 장르 19개에서 99번 장르인 '다큐멘터리'는 제외했음. (DB에 장르 99번 영화가 없기 때문)
original_genres.sort()                                      # 오름차순으로 정렬
print(original_genres)


    
random_top_movies = random.sample(top_movies, 35)           # 일단 랜덤으로 35개의 영화를 가져옴
selected_genres = []                                        # 랜덤으로 가져온 35개의 영화의 장르를 넣어줄 리스트
for random_top_movie in random_top_movies:
    genre_ids = random_top_movie['fields'].get('genre_ids') 
    for genre_id in genre_ids:
        selected_genres.append(genre_id)                    # 영화들의 장르 아이디들을 리스트에 담아줌

selected_genres = sorted(list(set(selected_genres)))        # set로 중복 제거하고 오름차순 정렬
print(selected_genres)

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
            random_genre_movie = random.sample(genre_movies, 1)
            if random_genre_movie not in random_top_movies:
                random_top_movies.append(random.sample(genre_movies, 1))
                print(len(random_top_movies))
                break
        


    while len(random_top_movies) < 40:
        while True:
            random_top_movie = random.sample(top_movies, 1)
            if random_top_movie not in random_top_movies:
                random_top_movies.append(random.sample(genre_movies, 1))
                break
    
    print(len(random_top_movies), 'end!!')
    print(type(random_top_movies))
    pprint(random_top_movies[0])
                  
    
else:
    print('oh')
    while len(random_top_movies) < 40:
        while True:
            random_top_movies.append(random.sample(top_movies, 1))
            if random_top_movie not in random_top_movies:
                random_top_movies.append(random.sample(top_movies, 1))
                break

    print(len(random_top_movies), 'end!!')
    # pprint(random_top_movies)





# ----------------------------------------------------------------
# 99번 장르(다큐멘터리는 하나도 없음 - 그래서 알고리즘 짤 때 고려 안해도 될듯)
# for all_top_movie in top_movies:
#     genre_ids = all_top_movie['fields'].get('genre_ids')   
#     if 99 in genre_ids:
#         print('yes')
#     else:
#         print('no')


