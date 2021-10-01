from django.shortcuts import render
from rest_framework.response import Response
from .models import Tweets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import TweetsSerializer
# Create your views here.


# def get_tweet(request):
#     qs = Tweets.objects.all()
#     return render(request, 'tweet/get_tweet.htm', {
#         'get_tweet': qs
#     })


# def get_username(request, username):
#     #username = request.GET['username', '']
#     #username = 'dayong'
#     qs = Tweets.objects.filter(username=username)

#     return render(request, 'tweet/get_username.htm', {
#         'get_username': qs
#     })


class TweetsListAPI(APIView):
    def get(self, request):
        queryset = Tweets.objects.all()
        # print(queryset)
        serializer = TweetsSerializer(queryset, many=True)
        return Response(serializer.data)


class TweetUsernameAPI(APIView):
    def get(self, request, username):
        queryset = Tweets.objects.filter(username=username)
        serializer = TweetsSerializer(queryset, many=True)
        return Response(serializer.data)


class TweetCreateAPI(ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
