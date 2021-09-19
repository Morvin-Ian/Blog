from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    info = {
        "posts":Post.objects.all()
         }

    return render(request,'post/index.html', info)
def blog(request,pk):
    inf = {
        "blogs":Post.objects.get(id=pk)
         }

    return render(request,'post/post.html', inf)
