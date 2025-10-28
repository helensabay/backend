from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Combo Meals', 'Combo Meals'),
        ('Meals', 'Meals'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    available = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
