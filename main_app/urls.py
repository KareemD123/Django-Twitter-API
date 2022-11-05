from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('tweets-list/', views.tweets_list),
    path('tweets-create/', views.tweet_create)
]