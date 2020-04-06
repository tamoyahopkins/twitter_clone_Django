
from django.views.generic import View
from django.urls import path
from tweet.views import tweet_view, Seetweet


urlpatterns = [
    path('', tweet_view, name='tweet'),
    # path('<int:id>/', see_tweet_view, name='tweet_content')
    path('<int:id>/', Seetweet.as_view(), name='tweet_content')



]