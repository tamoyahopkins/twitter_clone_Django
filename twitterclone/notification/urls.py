from notification.views import notification_view
from django.urls import path


urlpatterns = [
    path('<int:id>/', notification_view, name='notification'),


]
