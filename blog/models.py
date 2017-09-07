from django.db import models


# Create your models here.
class Post(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return self.title
