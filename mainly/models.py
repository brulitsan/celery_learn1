from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
