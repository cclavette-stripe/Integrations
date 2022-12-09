import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():
    link = stripe.PaymentLink.create(
        line_items=[{"price": 'price_1L60tLILwdSSnvJbzHAcYLpN', "quantity": 1}],
        allow_promotion_codes=True
    )
   
    print(link)

def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()


