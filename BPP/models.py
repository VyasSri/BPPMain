from django.db import models
from django.core.exceptions import ValidationError


class BinPackingDemo(models.Model):
    ALGORITHM_CHOICES = [
        ('first_fit', 'First Fit'),
        ('next_fit', 'Next Fit'),
        ('best_fit', 'Best Fit'),
        ('worst_fit', 'Worst Fit'),
    ]

    algorithm = models.CharField(max_length=20, choices=ALGORITHM_CHOICES)
    bin_capacity = models.PositiveIntegerField()
    item_list = models.TextField(help_text="Enter items as comma-separated values, e.g., 10, 20, 30")

