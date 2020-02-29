from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from twitteruser.models import MyCustomUser, Ticket
from twitteruser.forms import UserCreationForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'user_name')}
        ),
    )

class TicketAdmin(BaseUserAdmin):
    add_form = Ticket
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('posted_date', 'description', 'status', 'filed_by', 'assign_to_user', 'completed_by')}
        ),
    )

admin.site.register(MyCustomUser, UserAdmin)
# admin.site.register(Ticket, TicketAdmin)
admin.site.register(Ticket)





