from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import auth, User
from .serializer import gameLogSerializer
import datetime
from .models import gameLog
from django.core.exceptions import BadRequest

# Create your views here.


@api_view(["GET"])
def home(request):
    return Response("Hello World")


@api_view(["GET", "PUT"])
def stats(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            data = gameLog.objects.filter(user=request.user)
            serializer = gameLogSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)

        if request.method == "PUT":
            gameLog.objects.create(
                user=request.user, game=request.data["game"], duration=request.data["duration"], finish=request.data["finish"])
            return JsonResponse({"Status": "200 OK"})

    else:
        raise BadRequest('Invalid request.')


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/stats")
        else:
            return redirect("/login")


@api_view(["POST"])
def logout(request):
    auth.logout(request)
    return redirect("/login")
