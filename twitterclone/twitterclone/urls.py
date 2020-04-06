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
from twitteruser.views import login_view, logout_view, home_page_view, sign_up_view, user_profile_view, follow_user_view
from tweet.views import tweet_view
from notification.views import notification_view
from django.urls import include, path


urlpatterns = [
#load twitteruser urls
    path('admin/', admin.site.urls),

#loads tweet urls
    path('', include('twitteruser.urls')),
    path('tweet/', include('tweet.urls')),
    path('notifications/', include('notification.urls')),





















]