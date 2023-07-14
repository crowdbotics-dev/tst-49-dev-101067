from django.conf import settings
from django.db import models
class Home(models.Model):
    'Generated Model'
    location = models.CharField(max_length=255,)
    def hello_home(self):
        print("hello");
