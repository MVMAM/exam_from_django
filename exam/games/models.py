from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError, models

class NullPriceException(Exception):
    pass

class Game(models.Model):
    name_of_game = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    genre = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name_of_game + ' ' + self.author

    def save(self, *args, **kwargs):
        if self.genre == None or self.genre == "":
            raise IntegrityError("Genre cannot be null")
        if self.price == 0:
            raise NullPriceException
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)