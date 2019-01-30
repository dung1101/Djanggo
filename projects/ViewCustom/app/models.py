from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=55)


class Game(models.Model):
    name = models.CharField(max_length=55)
    man = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='game')
