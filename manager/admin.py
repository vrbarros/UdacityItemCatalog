from django.contrib import admin

from .models import Categories, CategoriesAdmin, Items, ItemsAdmin

# Register your models here.
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Items, ItemsAdmin)
