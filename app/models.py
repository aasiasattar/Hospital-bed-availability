from operator import mod
from pickle import FALSE
from pyexpat import model
from re import T
from django.db import models

# Create your models here.

class State(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.name



class Hospital(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)


    def __str__(self):
        return self.name


class Facility(models.Model):
    #hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False, default="")


    def __str__(self):
        return self.title


class Availability(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='availabilities')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='availabilities')
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'


