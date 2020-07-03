from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    balance = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.username


class Pet(models.Model):
    breed = models.CharField(max_length=500)
    nickname = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Lot(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    lot_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.lot_owner}, {self.pet}, {self.price}"


class Bet(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bet_value = models.IntegerField(validators=[MinValueValidator(0)])
    final_bet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lot}, {self.bet_value}, {self.author}"
