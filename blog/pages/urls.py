from django.urls import path
from .views import HomePageView, AbouPageView 

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), # localhost
    path('', AbouPageView.as_view(), name="about") # localhost
]