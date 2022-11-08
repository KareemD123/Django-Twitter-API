from django.shortcuts import render
from django.http import JsonResponse
# Create your views/functions here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TweetSerializer, CommentSerializer, UserSerializer
from .models import Tweet, Comment
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
# Retrieve User model
User = get_user_model()

# Class based views for our User Authentication

class RegisterView(APIView):

    def post(self, request):
        print('Hello world!')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful!!!'})
        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials!'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentials!'})
        
        token = jwt.encode(
            {'sub': user.id},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({'token': token, 'message': f'Welcome back {user.username}!!!'})






# Class based views inheriting from generics (ListCreate, RetrieveUpdateDestroy)

class TweetListCreateGen(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TweetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

# Class based views inheriting from the APIView

# class TweetListCreate(APIView):
#     def get(self, request):
        # tweets = Tweet.objects.all()
        # serializer = TweetSerializer(tweets, many=True)
        # return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     new_tweet = Tweet.objects.create(
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #     new_tweet.save()
    #     serializer = TweetSerializer(new_tweet)
    #     return Response(serializer.data)

# class TweetDetailUpdateDelete(APIView):
#     def get(self, request, pk):
#         tweet = Tweet.objects.get(id=pk)
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         tweet = Tweet.objects.get(id=pk)
#         serializer = TweetSerializer(tweet, request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         tweet = Tweet.objects.get(id=pk)
#         tweet.delete()
#         #redirect/re fetch all tweets
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)

#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

# Implement the Detail, Update, Delete using the api_view decorator

# @api_view(['GET'])
# def tweets_list(request):
#     tweets = Tweet.objects.all()
#     serializer = TweetSerializer(tweets, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def tweet_create(request):
#     serializer = TweetSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['GET'])
# def tweet_detail(request, pk):
#     tweet = Tweet.objects.get(id=pk)
#     serializer = TweetSerializer(tweet)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def tweet_update(request, pk):
#     tweet = Tweet.objects.get(id=pk)
#     serializer = TweetSerializer(tweet, request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def tweet_delete(request, pk):
#     tweet = Tweet.objects.get(id=pk)
#     tweet.delete()
#     # Refetch the data/redirect
#     tweets = Tweet.objects.all()
#     serializer = TweetSerializer(tweets, many=True)
#     return Response(serializer.data)














def home(request):
    data = {
        'app': 'Django'
    }
    return JsonResponse(data)









