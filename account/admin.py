from pyexpat import model
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from frontend import models

# Register your models here.


class register_product(admin.ModelAdmin):
    model = models.products
    list_display = ["title", "price", "category",
                    "thumbnail", "quantity", "description", "created_at"]


admin.site.register(models.products, register_product)
