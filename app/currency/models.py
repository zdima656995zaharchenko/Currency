from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField()
    currency_type = models.CharField(max_length=3)
    source = models.CharField(max_length=68)



from django.db import models

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)

    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.email_from} - {self.subject}"
