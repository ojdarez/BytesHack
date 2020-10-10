from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.IntegerField()
    color = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    addressLine1 = models.TextField()
    addressLine2 = models.TextField()
    
 
    def __str__(self):
        return self.firstName + " " + self.lastName
 
class FlightDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flightNum = models.IntegerField()
    checkInDt = models.DateField()
    checkInTm = models.TimeField()
    departDt = models.DateField()
    departTm = models.TimeField()

    
 
    def __str__(self):
        return f"{self.user} -- {self.flightNum}"


class HealthModel(models.Model):
    testWithinTenDays = models.BooleanField()
    beingtoHotSpot = models.BooleanField()
    age = models.IntegerField()
    pregnant = models.BooleanField()
    copd = models.BooleanField()
    testproof = models.FileField(upload_to="test", blank=True)


    def __str__(self):
        return f"Being to hotspot ? {self.beingtoHotSpot}"
 
 
