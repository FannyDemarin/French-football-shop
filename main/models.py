import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
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
    release_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Year of product release (e.g. 2024)"
    )

    def __str__(self):
        return self.name

    @property
    def is_item_hot(self):
        return self.item_views > 20

    def increment_views(self):
        self.item_views += 1
        self.save()
    