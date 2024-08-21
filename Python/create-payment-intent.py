import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    balance = stripe.PaymentIntent.create(
        amount=2000,
        currency="eur",
        # automatic_payment_methods={"enabled": True},
        description="this is a description",
        # confirm=True,
        # payment_method='pm_card_visa',
        payment_method_types=['card'],
        payment_method_options={
            'card': {
                'mandate_options': {
                    'amount': 2000,
                    'amount_type': 'fixed',
                    'reference': '8675309',
                    'interval': 'day',
                    'interval_count': 1,
                    'start_date': '1717785666',
                    'supported_types': ['india'],
                }
            }
        },
        # return_url='https://www.sdlkf.com',
        metadata={
            'key1': '',
            'key2': 'value2'
        }
    )
    print(balance)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
