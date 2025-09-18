from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostDeleteView,
    PostUpdateView
    )

urlpatterns = [
    path('list/', PostListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('new/', PostCreateView.as_view(), name="post_new"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
]