from django.db import models
import uuid
# from django.core.validators import FileExtensionValidator
from clubs.models import club_detail
from students.models import UserAccount

# Create your models here.

class event(models.Model):
    club= models.ForeignKey(club_detail, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=225, null= False)
    event_description = models.TextField(null= False)
    registration_start = models.DateTimeField(null = False)
    event_date = models.DateTimeField(null = False)
    event_end = models.DateTimeField(null = False)
    event_poster = models.ImageField(null = True)
class eventreg(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    event = models.ForeignKey(event,on_delete= models.CASCADE)
    club = models.ForeignKey(club_detail, on_delete=models.CASCADE)
