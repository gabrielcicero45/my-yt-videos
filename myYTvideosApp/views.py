from django.shortcuts import render,redirect
from django.contrib import messages
from pytube import YouTube

import os
import time

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        if request.POST['link']:
            link = request.POST['link']
            yt = YouTube(link).streams.first().download(os.path.expanduser("~"))
            print(link)
            time.sleep(10)
            return redirect('/downloaded')
        
    return render(request,'index.html')

def downloaded(request):

    return render(request,'downloaded.html')

    
    
