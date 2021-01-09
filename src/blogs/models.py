from django.db import models

# Create your models here.


class Post(models.Model):
    title       = models.CharField(max_length=120) #max_length
    description = models.TextField(blank=True, null=True)
    summery     = models.TextField(blank=True, null=True, default="Fill in this feild")
    posted      = models.BooleanField(default=False)

