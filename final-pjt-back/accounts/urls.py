from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.profile),

    # 좋아요한 영화 기반 알고리즘 추천
    path('<username>/recommend/', views.recommend),
]