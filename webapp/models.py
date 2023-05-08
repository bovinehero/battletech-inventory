from django.db import models

# Create your models here.
class Pilot(models.Model):
    """
    A Pilot will have a 1 2 1 relationship with a mech
    
    """
    callsign = models.CharField(max_length=50)
    gunnery = models.IntegerField(blank=True, default=4)
    piloting = models.IntegerField(blank=True, default=5)
    experience = models.IntegerField(blank=True, default=5)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.callsign