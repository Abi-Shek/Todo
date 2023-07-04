from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=250)
    is_compeleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.task
