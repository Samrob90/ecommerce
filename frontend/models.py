from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, default=None, null=False)
    price = models.FloatField(default=None, null=False)
    category = models.CharField(max_length=200, default=None, null=False)
    quantity = models.CharField(
        max_length=200, default="In stock", null=False)
    description = models.TextField(default=None, null=False)
    thumbnail = models.CharField(max_length=250, default=None)
    update_at = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.id


class images(models.Model):
    products = models.ForeignKey(
        products, on_delete=models.CASCADE, default=None, related_name="product_images")
    images = models.ImageField(upload_to="MEDIA/")
    created_at = models.DateTimeField(default=timezone.now)
