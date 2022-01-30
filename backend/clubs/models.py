from django.db import models
import uuid
# from django.core.validators import FileExtensionValidator

# Create your models here.

class club_detail(models.Model):
    club_name = models.CharField(max_length= 255, null = False)
    club_description = models.TextField(null = False)
    club_email = models.EmailField(null = False, unique=True)
    club_logo = models.ImageField(null = False, blank=False)
    #club_events = list of events held by the club