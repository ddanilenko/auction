from django.urls import path

from .views import *

urlpatterns = [
    path('lots', LotListView.as_view()),
    path('bets', BetListView.as_view()),
    path('bets/<int:pk>', BetDetailView.as_view()),
]
