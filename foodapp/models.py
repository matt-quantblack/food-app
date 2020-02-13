from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recipe(models.Model):
    apireference = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    iurl = models.CharField(max_length=150)
    weight = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foodsaved = models.IntegerField(default=0)
    co2saved = models.IntegerField(default=0)
    dollarsaved = models.IntegerField(default=0)

    cooked = models.ManyToManyField(Recipe)

class Box(models.Model):
    box_number = models.IntegerField(default=0)
    ingredient = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

