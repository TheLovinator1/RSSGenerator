from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    model = Post
    template_name = "index.html"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "detail.html"
