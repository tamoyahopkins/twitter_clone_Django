from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from twitteruser.models import MyCustomUser
from twitteruser.forms import UserCreationForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'user_name', 'following')}
        ),
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'following')}
        ),
    )

admin.site.register(MyCustomUser, UserAdmin)








