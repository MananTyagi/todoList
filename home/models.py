from django.db import models

class Tasks(models.Model):
    title= models.CharField(max_length=30)
    desc=models.TextField()
    date= models.DateTimeField(auto_now_add=True)
