from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import MyCustomUser
from tweet.models import Tweet

# Create your views here.
def notification_view(request, id):
    # print('current_user_id', id)
    current_user = MyCustomUser.objects.get(id=id)
    notification_items = Notification.objects.filter(for_user=id)
    total_notifications = 0
    show_notifications = [item for item in notification_items if not item.viewed]
    # print(show_notifications)
    if show_notifications:
        total_notifications = len(show_notifications)
    # print(total_notifications)
    total_tweets = Tweet.objects.filter(user=id).count()
    updated_notifications = Notification.objects.filter(for_user=id)
    for item in updated_notifications:
        item.viewed = True
        item.save()
    return render(request, 'Notifications.html', {
        'notifications': show_notifications,
        'current_user': current_user,
        'total_tweets': total_tweets,
        'total_notifications': total_notifications})
