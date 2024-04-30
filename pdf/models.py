from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    summary = models.TextField()
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    experience = models.TextField()
    skills = models.TextField()
    def __str__(self) -> str:
        return self.name
