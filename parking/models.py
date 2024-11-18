from django.db import models
from datetime import datetime
# Create your models here.

class category(models.Model):
    parking_choices = [
        ('activated', 'Activated'),
        ('deactivated', 'Deactivated'),
    ]  
    
    paring_area_no = models.CharField(max_length=100, null=False, blank=False)
    vehical_Type = models.CharField(max_length=100, null=False, blank=False)
    vehical_limit = models.CharField(max_length=200, null=False, blank=False)
    parking_charge = models.DecimalField(max_digits=10, decimal_places=2)  # Changed from CharField to DecimalField
    status = models.CharField(max_length=100, choices=parking_choices, default='activated')

    def __str__(self):
        return self.paring_area_no

class add(models.Model):
    vehical_choices = [
        ('parked', 'parked'),
        ('leaved', 'leaved'),
    ]
    vehical_number = models.CharField(max_length=200, null=False, blank=False)
    vehical_Type = models.CharField(max_length=100, null=False, blank=False)
    paring_area_no_id = models.ForeignKey(category, on_delete=models.CASCADE, default=True, null=False)
    parking_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default value added
    status = models.CharField(max_length=10, choices=vehical_choices, default='parked')
    parked_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.vehical_number



    

