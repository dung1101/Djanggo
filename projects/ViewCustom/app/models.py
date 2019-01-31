from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=55)
    money = models.IntegerField(default=1000000)

    def __str__(self):
        return '%s - %s$' % (self.name, self.money)


class Game(models.Model):
    name = models.CharField(max_length=55)
    man = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='game')
    release = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.man)

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'pk': self.pk})
