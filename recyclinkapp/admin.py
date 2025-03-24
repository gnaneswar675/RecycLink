from django.contrib import admin
from .models import UserProfile, MerchantProfile, RecyclingTransaction

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_joined', 'is_active')
    search_fields = ('full_name', 'email')
    list_filter = ('is_active', 'date_joined')

@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_type', 'email', 'is_verified')
    search_fields = ('business_name', 'email')
    list_filter = ('business_type', 'is_verified', 'registration_date')

@admin.register(RecyclingTransaction)
class RecyclingTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'merchant', 'material_type', 'weight', 'points_earned', 'transaction_date')
    search_fields = ('user__full_name', 'merchant__business_name')
    list_filter = ('material_type', 'is_completed', 'transaction_date')
