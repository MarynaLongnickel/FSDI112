# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('', include('pages.urls')),
# ]

from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # add signup view if you have one
]
