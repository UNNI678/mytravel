from django.db import models

# Create your models here.
class destiny(models.Model):
    name=models.CharField(max_length=280)
    img=models.ImageField(upload_to='clicks')
    des=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    imge=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=240)
    desc=models.TextField()

    def __str__(self):
        return self.name

