import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():
    charges = stripe.PaymentIntent.search(
        query="""metadata['key2']:'value2'""",
        
    )
    # print(charges.page)
    print(charges)


def main():
    # testing Stripe instance properly configured
    print(test())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
