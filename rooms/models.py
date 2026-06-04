from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    contact_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return self.title