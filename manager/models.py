from django.conf import settings
from django.db import models

# Create your models here.


class Categories(models.Model):
    """Categories model."""

    Name = models.CharField(max_length=30)
    Icon = models.CharField(max_length=250)


class Items(models.Model):
    """Items model."""

    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # Relate User model to this Item model and keep track of users
    User = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Keep track of data usage
    CreatedAt = models.DateTimeField(auto_now_add=True, blank=False)
    ChangedAt = models.DateTimeField(auto_now_add=True, blank=False)
