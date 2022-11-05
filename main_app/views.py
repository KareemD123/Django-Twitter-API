from django.shortcuts import render
from django.http import JsonResponse
# Create your views/functions here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet

@api_view(('GET',))
def tweets_list(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)

@api_view(('POST',))
def tweet_create(request):
    serializer = TweetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




def home(request):
    data = {
        'app': 'Django'
    }
    return JsonResponse(data)









