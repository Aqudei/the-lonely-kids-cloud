from django.contrib import admin
from .models import (Log, OrderInfo, LineItem, Bin,PrintRequest)
from .tasks import archive_bin_task
# Register your models here.


@admin.action(description="Empty selected bins")
def clear_bins(modeladmin, request, queryset):
    """
    docstring
    """
    for bin in queryset:
        archive_bin_task.delay(bin.Number)


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ['Number', 'Active']

    actions = [clear_bins]


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['OrderId', 'Bin', 'AllItemsPrinted', 'OrderNumber']
    list_filter = ['AllItemsPrinted']
    search_fields = ['OrderNumber']


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    list_display = ['OrderNumber', 'Name', 'DateModified',
                    'Status', 'Quantity', 'PrintedQuantity']
    search_fields = ['OrderNumber', 'Name']
    list_filter = ['Status']

    readonly_fields = ['DateModified']


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['ChangeDate', 'ChangeStatus', 'LineItem', 'order_number']
    search_fields = [
        'LineItem__OrderNumber',
        'LineItem__VariantTitle',
        'LineItem__Sku',
        'ChangeStatus'
    ]

    def order_number(self, obj):
        return obj.LineItem.OrderNumber

@admin.register(PrintRequest)
class PrintRequestAdmin(admin.ModelAdmin):
    list_display = ['LineItem','Done','Timestamp']
