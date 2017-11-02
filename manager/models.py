from django.conf import settings
from django.contrib import admin
from django.db import models

# Create your models here.


class CategoriesAdmin(admin.ModelAdmin):
    """Categories admin."""

    list_display = ('ID', 'Icon', 'Name')


class Categories(models.Model):
    """Categories model."""

    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Icon = models.CharField(max_length=250)

    def __str__(self):
        """Change field to more friendly value."""
        return self.Name

    class Meta:
        """Change table name to more friendly."""

        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class ItemsAdmin(admin.ModelAdmin):
    """Items admin."""

    list_display = ('ID', 'Title', 'Category',
                    'User', 'CreatedAt', 'ChangedAt')


class Items(models.Model):
    """Items model."""

    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # Relate User model to this Item model and keep track of users
    User = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Keep track of data usage
    CreatedAt = models.DateTimeField(auto_now_add=True, blank=False)
    ChangedAt = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        """Change field to more friendly value."""
        return self.Title

    class Meta:
        """Change table name to more friendly."""

        verbose_name = ("Item")
        verbose_name_plural = ("Items")
