from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_number = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

class Service(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='services')
    service_category = models.CharField(max_length=1, choices=(('s', 'salon service'), ('a', 'Appliance service'), ('c', 'Cleaning service'),('f', 'Fitness service'),('g', 'General service')))
    description = models.TextField(max_length=500,blank=False, null=False)
    location = models.CharField(max_length=1, choices=(('s', 'Salt lake city'), ('o', 'Omaha'), ('c', 'Chicago'),('d', 'Denver')))
    appointment_date_time = models.DateTimeField(
        default=timezone.now)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def appointment(self):
        self.appointment_date = timezone.now()
        self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)