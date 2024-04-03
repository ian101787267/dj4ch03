from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime

def homepage(request):
    posts = Post.objeccts.all()
    now =datetime.now() 
    return render(request, 'index.html',locals())
