from django.shortcuts import render
from .models import UserAccount
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def index(request):
    return render(request, 'userprofile/index.html')

def info(request, user_id):
    # info = UserAccount.objects.all()
    info = UserAccount.objects.get(pk=user_id)

    url = "/" + info.image.url.replace("userprofile/" ,"", 1)

    context = {
        'info': info,
        'url': url,
    }
    print(info.image.url)
    return render(request, 'userprofile/info.html', context)

def login(request):
    return render(request, 'userprofile/login.html')

def signup(request):
    return render(request, 'userprofile/signup.html')

def updateInfo(request, user_id):
    result = False

    user = UserAccount.objects.get(pk=user_id)
    data = json.loads(request.body.decode('utf-8'))

    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    user.bio = data['bio']
    user.save()

    return HttpResponse(status=200)

<<<<<<< HEAD
#This is a comment done locally
#test comment
#This is a new test comment
