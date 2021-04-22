from django.db import models
from django.urls import reverse
# Create your models here.

ATTIRE = (('Hat', 'Hat'), ('Shirt', 'Shirt'), ('Pants', 'Pants'), ('None',
                                                                   'None'))


class FanAttire(models.Model):
    clothing = models.CharField(max_length=5,
                                choices=ATTIRE,
                                default=ATTIRE[3][0])
    description = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.clothing} {self.description}'

    def get_absolute_url(self):
        return reverse("SportsParaphernalia_detail",
                       kwargs={"SportsParaphernalia_id": self.id})


class World_Cup(models.Model):
    location = models.CharField(max_length=40)
    year = models.IntegerField()
    champion = models.CharField(max_length=40)
    runner_up = models.CharField(max_length=40)
    mvps = models.TextField(max_length=255)
    champion_score = models.IntegerField()
    runner_up_score = models.IntegerField()
    fan_attire = models.ManyToManyField(FanAttire)

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


class Photo(models.Model):
    url = models.CharField(max_length=200)
    world_cup = models.ForeignKey(World_Cup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for world_cup_id: {self.world_cup_id} @{self.url}"