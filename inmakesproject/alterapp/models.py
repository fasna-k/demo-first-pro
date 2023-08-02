from django.db import models

# Create your models here.
class dtable(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos')
    description=models.TextField()

    def __str__(self):
        return self.name

class datatable(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos')
    description=models.TextField()

    def __str__(self):
        return self.name