from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Topic(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True) # database can have this value empty
    # participants =
    updated = models.DateTimeField(auto_now=True) # value will change whenever we save
    created = models.DateTimeField(auto_now_add=True) # value wont change anytime. It saves value only when its is first time saved

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return str(self.name)

# class Message(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     # room = models.ForeignKey(User,on_delete=models.CASCADE)
#     body = models.TextField()
#     update = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.body[0:50]