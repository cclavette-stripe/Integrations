import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    charge = stripe.Charge.create(
        amount=1500,
        currency='usd',
        source='acct_1L0ajSRAzYcRRMwc',
        description='This is not a refund'
    )
    print(charge)

def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
