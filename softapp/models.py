from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class UserQuery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    number = models.CharField(max_length=20)
    message = RichTextField()

    def __str__(self):
        return self.name
    