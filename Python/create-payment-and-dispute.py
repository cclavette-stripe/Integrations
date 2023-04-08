import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4000000000001976", # this card number creates an "inquiry" (see here --> https://stripe.com/docs/testing#disputes )
            "exp_month": 8,
            "exp_year": 2023,
            "cvc": "314",
        },
    )


def test():
    return stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        confirm="true",
        # automatic_payment_methods={"enabled": True},
        customer="cus_NPHON95MNtVXoh",
        payment_method=create_pm().id
    )


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
