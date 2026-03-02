from django.db import models

# Create your models here.
class VacuumBags(models.Model):
    supermarket = models.CharField(max_length=200)
    vacuum = models.CharField(max_length=200)
    size = models.CharField(max_length=200)

    def __str__(self):
        return f"Supermarkt: {self.supermarket}, Staubsauger-Modell: {self.vacuum}, Beutelgröße: {self.size}"


