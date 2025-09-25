from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostDeleteView, PostUpdateView,
    PostDraftListView, PostArchivedListView   # <-- new
)

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('drafts/', PostDraftListView.as_view(), name='drafts'),
    path('archived/', PostArchivedListView.as_view(), name='archived'),
]
