from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


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