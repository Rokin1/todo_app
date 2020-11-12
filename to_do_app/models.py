from django.db import models
# Create your models here.


class Todo(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=250)
