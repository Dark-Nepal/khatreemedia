from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
    

class testimonial(models.Model):
    feedback = models.TextField(max_length=200)
    fullname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
    
    