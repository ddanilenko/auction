Test Django project to run pet auction.

To build the service: `docker-compose up --build`

Database prefilled with 2 users ans 2 pets (details in initial_data.json).

User can:

1.Create a lot with an existing pet

URL: `/pet_auction/lots`

BODY: `{"pet": 1, "price": 1234, "lot_owner": 2}`

2.Other users can create a bet

URL: `/pet_auction/bets`

BODY: `{"lot": 1, "author": 3, "bet_value": 200}`

3.Lot author can mark bet as a "final bet"

URL: `/pet_auction/bets/<int:pk>`

BODY: `{"final_bet": true}`
