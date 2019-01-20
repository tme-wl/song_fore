from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=64)

class Element(models.Model):
    mine = models.CharField(max_length=64)
    whant = models.CharField(max_length=64)
    liaotianbao_id = models.CharField(max_length=128)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    info = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)