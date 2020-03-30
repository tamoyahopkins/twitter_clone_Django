from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from tweet.forms import Tweet_form
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from twitteruser.models import MyCustomUser
from django.http import HttpResponseRedirect
from notification.models import Notification
import re

# Create your views here.
@login_required
def tweet_view(request):
    current_user = MyCustomUser.objects.get(id=request.user.id).username
    # new_user = MyCustomUser.objects.get(id=request.user.id)
    if request.method == "POST":
        form = Tweet_form(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data)
            new_tweet = Tweet.objects.create(
                user = MyCustomUser.objects.get(pk=request.user.id),
                text = data['text']
            )
            found_users = re.findall(r'(@[\w]+)', data['text'])
            for item in found_users:
                item = item[1:]
                if item in str(MyCustomUser.objects.all()):
                    print('for_user', MyCustomUser.objects.get(username=item))
                    print('new_tweet', new_tweet)
                    Notification.objects.create(
                        for_user = MyCustomUser.objects.get(username=item),
                        source_tweet = new_tweet
                    )
                    print('Notifications:', Notification.objects.all())
            return HttpResponseRedirect(f'/user/')
    form = Tweet_form()
    return render(request, 'tweet.html', {'form': form, 'current_user': current_user})

# def see_tweet_view(request, id):
#     tweet_content = Tweet.objects.get(pk=id)
#     return render(request, 'tweet_content.html', {'tweet': tweet_content})

class Seetweet(View):
    def get(self, request, id):
        tweet_content = Tweet.objects.get(pk=id)
        return render(request, 'tweet_content.html', {'tweet': tweet_content})
