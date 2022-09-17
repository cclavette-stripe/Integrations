import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = "2018-02-28"

# DEFINE FUNCTIONS


def test():

    session = stripe.checkout.Session.create(
        line_items=[{
            'name': 'Stainless Steel Water Bottle',
            'amount': 1000,
            'currency': 'usd',
            'quantity': 1,
        }],
        payment_intent_data={
            'application_fee_amount': 123,
        },
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
        stripe_account='acct_1KqOHIDLXCJQbu9g',
    )
    print(session)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
