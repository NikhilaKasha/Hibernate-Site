
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Customer, Service

class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name' , 'cust_number', 'email')
    list_filter = ( 'cust_name', 'cust_number')
    search_fields = ('cust_name', 'cust_number')
    ordering = ['cust_name']

class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category','location', 'appointment_date_time')
    list_filter = ( 'cust_name', 'service_category','location')
    search_fields = ('cust_name', 'location','zipcode')
    ordering = ['cust_name','service_category',]
admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)