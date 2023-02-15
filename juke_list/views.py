from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    video = Video.objects.all()
    context = {
        'video' : video,
    }
    return render(request,'home.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password!=confirm:
            return HttpResponse("Password not matching!!")
        else:
            authenticate(username=username, password=password)
            return redirect('home')
    return render(request,'login.html')
