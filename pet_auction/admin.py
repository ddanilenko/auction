from django.contrib import admin

from .models import User, Pet, Lot, Bet

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Lot)
admin.site.register(Bet)
