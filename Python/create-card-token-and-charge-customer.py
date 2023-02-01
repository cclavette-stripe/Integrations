import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    # Create a Customer:
    customer = stripe.Customer.create(
        source='tok_us',
        email='paying.user@example.com',
    )

    # Charge the Customer instead of the card:
    charge = stripe.Charge.create(
        amount=1000,
        currency='usd',
        customer=customer.id,
    )

    # YOUR CODE: Save the customer ID and other info in a database for later.

    # When it's time to charge the customer again, retrieve the customer ID.
    charge1 = stripe.Charge.create(
        amount=1500,  # $15.00 this time
        currency='usd',
        customer=customer.id,  # Previously stored, then retrieved
    )

    charge2 = stripe.Charge.create(
        amount=1500,  # $15.00 this time
        currency='usd',
        customer=customer.id,  # Previously stored, then retrieved
    )
    print(charge1)
    print(charge2)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
