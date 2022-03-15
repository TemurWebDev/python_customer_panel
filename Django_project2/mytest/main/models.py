from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phon_number = models.CharField(max_length=13)
    addres = models.TextField()

    def __str__(self):
        return self.first_name