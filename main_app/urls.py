from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    #The path below are for Token Authentication
    path('signup/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    # The paths below use generics
    path('tweets-list-create-generics/', views.TweetListCreateGen.as_view()),
    path('tweets-retrieve-update-destroy-generics/<int:pk>/', views.TweetRetrieveUpdateDestroy.as_view())

    #----------------------------------------------------
    #The path below implemenet class based views inheriting from the APIView class
    # path('tweets-list-create-api/', views.TweetListCreate.as_view()),
    # path('tweets-detail-update-delete-api/<int:pk>/', views.TweetDetailUpdateDelete.as_view())
    #----------------------------------------------------
    # The paths below are for implementing api_view decorator functions
    # path('tweets-list/', views.tweets_list),
    # path('tweets-create/', views.tweet_create),
    # path('tweets-detail/<int:pk>/', views.tweet_detail),
    # path('tweets-update/<int:pk>/', views.tweet_update),
    # path('tweets-delete/<int:pk>/', views.tweet_delete)
    #----------------------------------------------------
]