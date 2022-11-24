from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import User, ProfileImage
from .forms import ProfileImageForm

import requests
import json
import pprint
import random


# Create your views here.
@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    print(person.review_set.all())
    context = {
        'userid': person.id,
        'username': person.username,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
        'like_movies': list(person.like_movies.values()),
        'like_reviews': list(person.like_reviews.values()),
        'my_reviews': list(person.review_set.all().values()),
    }
    return Response(context)


# 11.24 민혁 추가 special thanks to David.U
@api_view(['POST'])
def profile_image(request, user_id):

    # 프로필 이미지 조회
    if request.method == 'GET':
        image = get_object_or_404(ProfileImage, user=user_id)
        return Response(image)

    # 프로필 이미지 설정
    elif request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_user_model()
            user = user.objects.get(pk=user_id)
            image_saved = form.save(commit=False)
            image_saved.user = user
            image_saved.save()
            return Response({'result': 'success'}) # 그냥 Response 해줘야해서 추가한 값
            
    # 프로필 이미지 수정
    elif request.method == 'PUT':
        profile_image = get_object_or_404(ProfileImage, user=user_id)
        form = ProfileImageForm(request.POST, request.FILES, instance=profile_image)
        if form.is_valid():
            form.save()
            return Response({'result': 'success'})

@api_view(['GET'])   
def show_image(request, user_id):
    
    profile_image = get_object_or_404(ProfileImage, user=user_id)
    # print(type(str(profile_image.profile_image)), '**************')
    # print(profile_image.profile_image)

    profile_image = str(profile_image.profile_image)
    # print(profile_image, '**************************')

    # context = {
    #     'profile_image': profile_image
    # }
    return Response(profile_image)

    
