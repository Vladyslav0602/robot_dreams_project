from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'purchase_date')
    search_fields = ('user__username', 'book__title')


admin.site.register(Purchase, PurchaseAdmin)
