from django.apps import AppConfig
#app config defines everything custom about that piece of a django app.  Apps makes it very easy to compartmentalize
# simplify imports, makes it very portable (can copy the dir into a diff project and add it to installed apps and
# # it will just work)
#also where you configure anything else for the application


class CustomUserAppConfig(AppConfig):
    name = 'twitteruser'
