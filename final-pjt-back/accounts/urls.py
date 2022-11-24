from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.profile),
    path('image/<int:user_id>/', views.profile_image),
    path('show_image/<int:user_id>/', views.show_image)
]