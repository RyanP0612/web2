from django.apps import AppConfig
from .jobs import * 

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    def ready(self):
        print("My django app is ready!!!")
        StartChatBotScheduler()