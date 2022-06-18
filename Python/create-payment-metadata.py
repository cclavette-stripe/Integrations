import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS

def test_balance():
    stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        payment_method_types=["card"],
        metadata={
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
        }
    )


def main():
    # testing Stripe instance properly configured
    print(test_balance())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
