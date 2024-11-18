from django.contrib import admin
from .models import category, add

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display="paring_area_no","vehical_type","vehical_limit","parking_charge"

admin.site.register(category)  
admin.site.register(add)  







































