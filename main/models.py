import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('t-shirt', 'T-shirt'),
        ('ball', 'Ball'),
        ('scarf', 'Scarf'),
        ('tracksuit', 'Tracksuit'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='t-shirt')
    is_featured = models.BooleanField(default=False)
    item_views = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255)
    release_year = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def is_item_hot(self):
        return self.item_views > 20

    def increment_views(self):
        self.item_views += 1
        self.save()
    