from django.shortcuts import render , HttpResponse,redirect
from . import forms
from .models import Post
from .forms import CreateArticle
from rest_framework import viewsets,permissions
from .srializers import PostSerializer
# Create your views here.
def article_list(request):
    articles = Post.objects.all().order_by('first_name')
    return render(request,'article_list.html', {'articles':articles})



def article_detail(request, slug):
    article = Post.objects.get(slug=slug)
    return render(request,'article_detail.html',{'article':article})


def article_create(request):
    forms_class = CreateArticle
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("my_app:list")
    else:
        form = forms.CreateArticle()
    return render(request,'article_create.html', {"form":form})




class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
