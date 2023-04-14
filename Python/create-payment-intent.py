import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    balance = stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        automatic_payment_methods={"enabled": True},
        description="this is a description"
    )
    print(balance)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
