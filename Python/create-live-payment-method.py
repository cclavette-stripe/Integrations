import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY_LIVE = os.getenv('STRIPE_SECRET_KEY_LIVE')
stripe.api_key = STRIPE_SECRET_KEY_LIVE

# DEFINE FUNCTIONS


def test():

    pm = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4867966905948184",
            "exp_month": 2,
            "exp_year": 2025,
            "cvc": "318",
        },
    )
    print(pm)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
