from django.contrib import admin
from .models import (
    Table, Order
)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
