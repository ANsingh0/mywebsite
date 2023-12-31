from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    desc = models.TextField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name 