from django.db import models

# Create your models here.

class Room(models.Model):
    # host =
    #topic =
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True) # database can have this value empty
    # participants =
    updated = models.DateTimeField(auto_now=True) # value will change whenever we save
    created = models.DateTimeField(auto_now_add=True) # value wont change anytime. It saves value only when its is first time saved

    def __str__(self):
        return str(self.name)