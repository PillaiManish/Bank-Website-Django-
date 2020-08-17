from django.contrib import admin

# Register your models here.
from .models import customer_complaints
class complaint_list(admin.ModelAdmin):
    list_display = ('userid','date','subject','complaint','return_date','return_message')
admin.site.register(customer_complaints,complaint_list)