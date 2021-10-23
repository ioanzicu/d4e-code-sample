
from django.db import models
from django.core.validators import MinLengthValidator


class Breed(models.Model):
    name = models.CharField(max_length=200,
                            validators=[MinLengthValidator(2, "Breed must be greater than 1 character")])

    def __str__(self) -> str:
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=200,
                                validators=[MinLengthValidator(2, "Name must be greater than 1 character")])
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    weight = models.FloatField()
    foods = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
