from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    list_per_page = 10
    list_editable = ('status',)
    list_max_show_all = 20


# Register your models here.
