from django.db import models
from django.urls import reverse
# Create your models here.


class World_Cup(models.Model):
    location = models.CharField(max_length=40)
    year = models.IntegerField()
    champion = models.CharField(max_length=40)
    runner_up = models.CharField(max_length=40)
    mvps = models.TextField(max_length=255)
    champion_score = models.IntegerField()
    runner_up_score = models.IntegerField()

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cup_id': self.id})


PREFER = (('A', 'Team A'), ('B', 'Team B'))


class Fan(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    country_of_residency = models.CharField('Country/Planet of Residence',
                                            max_length=20)
    supports = models.CharField(max_length=1,
                                choices=PREFER,
                                default=PREFER[0][0])

    world_cup = models.ForeignKey(World_Cup, on_delete=models.CASCADE)