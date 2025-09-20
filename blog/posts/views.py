from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# CRUD -> Create, Read, Update and Delete App
# The generic classes are ListView, CreateView, UpdateView, DeleteView and DetailView
#               GET       POST      POST       POST      GET
# Create your views here.

"""
PostListView is going to retrieve all of the object from the Post table in the db
"""
class PostListView(ListView): #Inheritance
    #template_name attribute is going to render an specific html file
    template_name = "posts/list.html"
    #model is going to be from which table we want to retrieve the data
    # model = Post
    queryset = Post.objects.all()
    #context_object_name would allow us to modify the name and how to call it in the htmls
    context_object_name = "post_list"

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("posts")

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]