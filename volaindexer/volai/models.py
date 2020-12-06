from django.db import models
from datetime import datetime
# Create your models here.
class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    room_adress = models.CharField(max_length=100, unique=True)
    room_shortadress = models.CharField(max_length=100, blank=True, null=True )
    room_pass = models.CharField(max_length=100, blank=True)
    room_add = models.DateTimeField("Date Posted", default =datetime.now)
    room_viewers = models.PositiveIntegerField(default=0)
    room_reports = models.PositiveIntegerField(default=0)

    #def __str__(self):
        #return self.room_name
