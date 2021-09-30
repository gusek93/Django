from django.shortcuts import render
from .models import Tweets

# Create your views here.


def get_tweet(request):
    qs = Tweets.objects.all()
    return render(request, 'tweet/get_tweet.htm', {
        'get_tweet': qs
    })


def get_username(request):
    #request.GET['username', '']
    username = 'dayong'
    qs = Tweets.objects.filter(username=username)

    return render(request, 'tweet/get_username.htm', {
        'get_username': qs
    })
