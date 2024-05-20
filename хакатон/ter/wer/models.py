from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='images/')
    text =models.TextField()
    raitng = models.FloatField(blank=True)
    like = models.IntegerField(blank=True)
    is_published = models.BooleanField(default=True)
    creted_at = models.DateField(auto_now_add=True)
class Reviz(models.Model):
    name = models.CharField(max_length=150)
    text =models.TextField()
    creted_at = models.DateField(auto_now_add=True)
class Prodkt(models.Model):
    title = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='images/')
    text =models.TextField()
    price =models.PositiveIntegerField()
