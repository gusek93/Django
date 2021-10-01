from rest_framework.serializers import ModelSerializer
from .models import Tweets


class TweetsSerializer(ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'
