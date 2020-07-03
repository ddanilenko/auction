from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import *


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'

    def validate_lot_owner(self, lot_owner):
        """Check that lot created for user that own pet"""
        data = self.get_initial()
        try:
            pet = Pet.objects.get(pk=data['pet'])
            if lot_owner != pet.owner:
                raise ValidationError(f'You cannot add lot while lot owner '
                                      f'is not the owner of chosen pet.')
        except (Pet.DoesNotExist, KeyError):
            pass
        return lot_owner


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'

    def validate_bet_value(self, bet_value):
        """Check that bet value correspond to existing balance
        (commented: bet value is bigger than lot price)
        """
        data = self.get_initial()
        try:
            author = User.objects.get(pk=data['author'])
            if bet_value > author.balance:
                raise ValidationError(f'You cannot use {bet_value}. '
                                      f'You have {author.balance} on your balance.')
        except (User.DoesNotExist, KeyError):
            pass

        # This part can be used if bet can't be less than lot price
        # try:
        #     lot = Lot.objects.get(pk=data['lot'])
        #     if bet_value < lot.price:
        #         raise ValidationError(f'You cannot use {bet_value}. '
        #                               f'Bet should be more than lot price ({lot.price}).')
        # except (Lot.DoesNotExist, KeyError):
        #     pass
        return bet_value

    def validate_author(self, author):
        """Check that user can't make net for own lot"""
        data = self.get_initial()
        try:
            lot = Lot.objects.get(pk=data['lot'])
            if author == lot.lot_owner:
                raise ValidationError(f'You cannot add bets to your lot')
        except (Lot.DoesNotExist, KeyError):
            pass
        return author


class BetPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['final_bet']
