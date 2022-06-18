import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def create_quote():
    quote = stripe.Quote.create(
        customer="cus_EiZOLZ4ZPiejyu",
        line_items=[
            {
                "price": "price_1L2fcpILwdSSnvJbY7DFYWXe",
                "quantity": 2,
            },
        ],
        discounts=[
            {'coupon': 'S5qIIcfa'}
        ]
    )
    print(quote)


def main():
    # testing Stripe instance properly configured
    print(create_quote())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
