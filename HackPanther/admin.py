from django.contrib import admin

# Register your models here.
from .models import User, FlightDetail, HealthModel
 
admin.site.register(User)
admin.site.register(FlightDetail)
admin.site.register(HealthModel)
