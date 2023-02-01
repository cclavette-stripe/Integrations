import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():
    token = stripe.Token.create(
        card={
            "number": "4242424242424242",
            "exp_month": 1,
            "exp_year": 2024,
            "cvc": "314",
        },
    )
    # Charge the Customer instead of the card:
    charge = stripe.Charge.create(
        amount=1000,
        currency='usd',
        source=token.id,
    )

    # When it's time to charge the customer again, retrieve the customer ID.
    charge1 = stripe.Charge.create(
        amount=1500,  # $15.00 this time
        currency='usd',
        source=token.id,  # Previously stored, then retrieve
    )
    print(charge1)
    print(charge2)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
