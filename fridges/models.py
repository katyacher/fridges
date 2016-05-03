from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class fridges (models.Model):
    fridgeGroup = models.CharField(max_length = 150)
    fridgeLocation = models.TextField()
    fridgesID = models.IntegerField()
    fridgeTemp = models.IntegerField()
    fridgeStatus = models.CharField(max_length = 150)
    
class fridgesdata (models.Model):
    fridgesdataID = models.ForeignKey("fridges")
    fridgesdataTemp = models.IntegerField()
    fridgesdataTime = models.DateTimeField()     
    
class fridgesAdmin(admin.ModelAdmin):
    list_display = ('fridgeGroup', 'fridgeTemp', 'fridgeLocation','fridgesID', 'fridgeStatus')
     
admin.site.register(fridges, fridgesAdmin)