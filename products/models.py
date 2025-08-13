from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('car_diecast', 'Car Diecast'),
        ('poster', 'Poster'),
        ('mouse_pad', 'Mouse Pad'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name