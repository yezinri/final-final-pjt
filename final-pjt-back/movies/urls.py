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
    # 좋아요한 영화 기반 알고리즘 추천
    path('<username>/recommend/', views.recommend),

    path('random_movies/', views.random_movies),
    # 영화 DB API로 받아오기
    path('getdb', views.get_db),
]