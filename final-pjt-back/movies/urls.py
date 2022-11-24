from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/likes/', views.movie_likes),
    path('<int:movie_pk>/reviews/', views.review_list),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/reviewcreate/', views.review_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/likes/', views.review_likes),

    # 영화 detail 페이지에 보여줄 관련영화 추천(11.23 추가)
    path('<int:movie_pk>/similar_movies/', views.similar_movies),
    # 좋아요한 영화 기반 알고리즘 추천
    path('<username>/recommend/', views.recommend),

    # 오늘의 영화 (11.23-24 사이 언젠가 추가)
    path('today_movie/', views.today_movie),
    path('worst_movie/', views.worst_movie),
    path('random_movies/', views.random_movies),
    path('latest_movies/', views.latest_movies),
    # 영화 DB API로 받아오기
    path('getdb/', views.get_db),
    path('search/<searchword>/', views.search),
]