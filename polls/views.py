from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request, pid=None):
    if pid == None:
        pid = 0
    qsData = Post.objects.all()

    data = {'list': [record['title'] for record in qsData.values()]}
    temp = [record['description'] for record in qsData.values()]
    data.update({'description': temp[pid]})
    return render(request, "polls/index.html", data)

def write(request):
    qsData = Post.objects.all()
    data = {'list': [record['title'] for record in qsData.values()]}
    return render(request, "polls/write.html", data)

def process(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if not title:
        messages.warning(request, "제목을 입력해 주세요.")
    elif not description:
        messages.warning(request, "내용을 입력해 주세요.")
    else:
        Post.objects.create(title=title, description=description, time=datetime.now())
        messages.success(request, "성공적으로 작성하였습니다.")

    return redirect('polls:write')
