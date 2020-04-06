from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, reverse
from twitteruser.models import MyCustomUser
from twitteruser.forms import UserCreationForm, LogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from tweet.models import Tweet
from notification.models import Notification


def login_view(request):
    if request.user.is_authenticated:
        # print('REQUEST', request)
        return HttpResponseRedirect(f'/user/')
    else:
        if request.method == 'POST':
            form = LogInForm(data=request.POST)

            if form.is_valid():
                # print('LOGIN INFO:', login(request, form.get_user()))
                login(request, form.get_user())
                return HttpResponseRedirect(f'/user/')
        else:
            form = LogInForm()

        return render(request, 'Login.html', {'form': form})



def home_page_view(request):
    if request.user.is_authenticated:
        current_user = MyCustomUser.objects.get(id=request.user.id)
        current_user_name = f'@{current_user.username}'
        followers = [item.username for item in current_user.following.all()]
        followers_tweets = []

        tweet_list = Tweet.objects.filter(user=current_user).order_by('-date')
        total_tweets = len(tweet_list)
        all_tweets = Tweet.objects.all().order_by('-date')

        for tweet in all_tweets:
            if str(tweet.user) != current_user.username:
                if str(tweet.user) in followers:
                    followers_tweets.append(tweet)


        notification_items = Notification.objects.filter(for_user=request.user.id)
        total_notifications = 0
        show_notifications = [item for item in notification_items if not item.viewed]
        if show_notifications:
            total_notifications = len(show_notifications)

        return render(request, 'Profile.html', {
            'current_user': current_user,
            'current_user_name': current_user_name,
            'tweet_list': tweet_list,
            'total_tweets': total_tweets,
            'all_tweets': all_tweets,
            'total_notifications': total_notifications,
            'followers_tweets': followers_tweets
        })
    return HttpResponseRedirect(f'/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(f'/')


def sign_up_view(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data)
            MyCustomUser.objects.create_user(
                user_name = data['user_name'],
                username = data['user_name'],
                email = data['email'],
                password = data['password1'],
                first_name = data['first_name'],
                last_name = data['last_name']
            )
            new_user = MyCustomUser.objects.get(email=data['email'])
            login(request,new_user)
            # return render(request, 'Login.html', {'form': LogInForm, 'confirm': f"{data['user_name'].title()}'s profile created successfully!  Please login."})
            return HttpResponseRedirect(f'/user/')
    form = UserCreationForm()
    return render(request, 'Signup.html', {'form': form})

def user_profile_view(request, id):
    current_user = MyCustomUser.objects.get(id=id)
    current_user_name = f'@{current_user.username}'
    tweet_list = Tweet.objects.filter(user=current_user).order_by('-date')
    total_tweets = len(tweet_list)
    return render(request, 'User_Profile.html', {
        'current_user': current_user,
        'current_user_name': current_user_name,
        'tweet_list': tweet_list,
        'total_tweets': total_tweets,
    })

@login_required
def follow_user_view(request, id):
    current_user = MyCustomUser.objects.get(id=id)
    logged_in_user = MyCustomUser.objects.get(id=request.user.id)
    logged_in_user.following.add(current_user)
    # data = False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

