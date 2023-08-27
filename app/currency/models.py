from django.db import models

class Rate(models.Model):
    currency = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.currency} - {self.rate}"

class ContactUs(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name