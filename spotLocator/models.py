from django.db import models
from django.urls import reverse


class Spot(models.Model):
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=200, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    imageURL = models.CharField(max_length=140, blank=True, null=True)
    ROADCYCLE = 'Road-Cycling'
    MTNBIKE ='Mountain Biking'
    HIKE = 'Hiking'
    FISH = 'Fishing'
    CLIMB = 'Rock Climbing'
    ACTIVITY_CHOICES = ( 
        (ROADCYCLE, 'Road-Cycling'),
        (MTNBIKE, ' Mountain Biking'),
        (HIKE, 'Hiking'),
        (FISH, 'Fishing'),
        (CLIMB, 'Rock Climbing'),
    )
    activity = models.CharField(
        max_length=15,
        choices=ACTIVITY_CHOICES,
        default=FISH,
        
    )
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('spot-detail', kwargs={'pk': self.pk})