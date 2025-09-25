from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin   # <-- new

class PostListView(ListView):
    template_name = "posts/list.html"
    context_object_name = "post_list"
    status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("posts:detail", kwargs={"pk": self.object.pk})
    
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("posts")

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "posts/drafts.html"
    context_object_name = "draft_list"

    def get_queryset(self):
        status = Status.objects.get(name="draft")
        return Post.objects.filter(status=status, author=self.request.user).order_by("created_on").reverse()

class PostArchivedListView(LoginRequiredMixin, ListView):
    template_name = "posts/archived.html"
    context_object_name = "archived_list"

    def get_queryset(self):
        status = Status.objects.get(name="archived")
        return Post.objects.filter(status=status, author=self.request.user).order_by("created_on").reverse()
