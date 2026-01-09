from django.db import models
from django.contrib.auth.models import User


class CarMake(models.Model):
    """Model for car manufacturers"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Model for specific car models"""
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
    ]
    
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default='Sedan')
    year = models.IntegerField()
    
    class Meta:
        ordering = ['make', 'name', 'year']
    
    def __str__(self):
        return f"{self.year} {self.make.name} {self.name}"
