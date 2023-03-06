import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
# STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

######## Stripe Shop API key DO NOT GIT PUSH ###############
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# DEFINE FUNCTIONS


def test():

    topup = stripe.Topup.create(
        destination_balance='issuing',
        amount=200000,
        currency='usd',
        description="Top-up for Issuing, July 18, 2022",
        statement_descriptor='Top-up',
    )

    cardholder = stripe.issuing.Cardholder.create(
        name='Jenny Rosen',
        email='jenny.rosen@example.com',
        phone_number='+18008675309',
        status='active',
        type='individual',
        billing={
            'address': {
                'line1': '123 Main Street',
                'city': 'San Francisco',
                'state': 'CA',
                'postal_code': '94111',
                'country': 'US'
            }
        }
    )

    card = stripe.issuing.Card.create(
        cardholder='ich_1Cm3pZIyNTgGDVfzI83rasFP',
        type='virtual',
        currency='usd',
        status='active'
    )
    print(topup)


def main():
    # testing Stripe instance properly configured
    print(test())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
