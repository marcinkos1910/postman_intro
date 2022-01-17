from django.db import models


class OurModel(models.Model):
    name = models.CharField(max_length=20)
    number = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
