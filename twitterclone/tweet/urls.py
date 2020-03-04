
from django.urls import path
from tweet.views import tweet_view, see_tweet_view


urlpatterns = [
    path('', tweet_view, name='tweet'),
    path('<int:id>/', see_tweet_view, name='tweet_content')


]