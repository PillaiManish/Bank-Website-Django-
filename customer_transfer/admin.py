from django.contrib import admin

# Register your models here.
from .models import customer_transfer
class transfer_list(admin.ModelAdmin):
    list_display = ('self_userid','to_userid','date','to_amount')
admin.site.register(customer_transfer,transfer_list)