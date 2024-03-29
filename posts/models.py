from django.db import models
from django.conf import settings    

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Upon deletion of user, post will also get deleted
    created_at = models.DateTimeField(auto_now_add=True) # Auto_now_add for first object creation
    updated_at = models.DateTimeField(auto_now = True) # auto_now is for every time object is modified

    def __str__(self):
        return self.title