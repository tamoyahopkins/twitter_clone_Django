"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import View
from twitteruser.views import user_profile_view, follow_user_view, sign_up_view
from twitteruser.views import Homepage, Login, Logout
from django.urls import include, path

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('user/', Homepage.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', sign_up_view, name='signup'),

    path('profile/<int:id>/', user_profile_view, name='userprofile'),
    path('follow/<int:id>/', follow_user_view, name='followuser')




















]