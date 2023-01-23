import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    payment = stripe.PaymentIntent.modify(
        "pi_3MPsjrILwdSSnvJb1F6TPkcZ",
        receipt_email="cclavette@stripe.com",
    )
    print(payment)


def main():
    # testing Stripe instance properly configured
    print(test())
    


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
