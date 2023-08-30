from django.db import models

# Create your models here.

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name

