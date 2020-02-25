from django.contrib import admin
from django.urls import path
from twitteruser.views import login_view, home_page_view, logout_view, create_user_view, ticket_detail_view, edit_ticket_view, ticket_completed_view
from twitteruser.views import add_ticket_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='home'),
    # path('<int:userid>', home_page_view, name='home'),
    path('user/<int:id>', home_page_view, name='user_page'),
    path('logout', logout_view, name='logout'),
    path('addticket', add_ticket_view, name='addticket'),
    path('adduser', create_user_view, name='adduser'),
    path('ticket/<int:id>', ticket_detail_view, name='ticket'),
    path('editticket/<int:id>', edit_ticket_view, name='editticket'),
    path('ticket/<int:ticket_id>/completed', ticket_completed_view, name='ticketcompleted')









]