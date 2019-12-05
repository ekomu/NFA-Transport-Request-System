from django.db import models


class Town(models.Model):
    DIRECTORATE_CHOICES = (('ED','ED'), ('DFA','DFA'), ('DNF','DNF'))
    TRANSPORT_OFFICER = 'TO'

    date = models.DateField()
    name = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()
    details_of_route = models.CharField(max_length=50)
    time_from = models.TimeField()
    time_to = models.TimeField()
    return_date = models.DateField()
    number_of_personnel = models.PositiveSmallIntegerField()
    directorate = models.CharField(max_length=10, choices=DIRECTORATE_CHOICES)
    trans_officer = models.CharField(TRANSPORT_OFFICER, max_length=10)
