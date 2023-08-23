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


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    exchange_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
