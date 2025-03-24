from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} - User Profile"

class MerchantProfile(models.Model):
    BUSINESS_TYPES = [
        ('collector', 'Collection Center'),
        ('recycler', 'Recycler'),
        ('manufacturer', 'Manufacturer')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.business_name} - {self.get_business_type_display()}"

class RecyclingTransaction(models.Model):
    MATERIAL_TYPES = [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
        ('electronics', 'Electronics')
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    merchant = models.ForeignKey(MerchantProfile, on_delete=models.CASCADE)
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPES)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    points_earned = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.full_name} - {self.material_type} - {self.transaction_date}"

    class Meta:
        ordering = ['-transaction_date']