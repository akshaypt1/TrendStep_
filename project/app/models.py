from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)  # You may hash passwords later

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    rating = models.FloatField(default=0.0)
    category = models.CharField(max_length=50, choices=[('Men', 'Men'), ('Women', 'Women')],default='Men')

    def __str__(self):
        return self.name