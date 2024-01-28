from django.db import models

# Create your models here.
class Project(models.Model):
    tite = models.CharField(max_length=200)
    script = models.FileField('/scripts', null=True, blank=True)
    createor_note = models.TextField()
    link 
    password_access 
    comprabale_titles