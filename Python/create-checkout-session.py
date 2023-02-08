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
            'price': 'price_1MF3haILwdSSnvJbkv1vG2Uh',
            'quantity': 1
        }],
        mode='subscription',
        allow_promotion_codes=True,
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
        idempotency_key='u6rjmgMlligPRlUf'
    )
    print(session)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
