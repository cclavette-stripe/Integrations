import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    card = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 12,
            "exp_year": 2034,
            "cvc": "314",
        },
    )
    payment = stripe.PaymentIntent.create(
        amount=2000,
        currency="usd",
        description="this is a description",
        capture_method='manual',
        confirm=False,
        payment_method=card.id,
    )

    confirm = stripe.PaymentIntent.confirm(
        payment.id,
        payment_method=card.id,
    )

    stripe.PaymentIntent.modify(
        payment.id,
        customer='cus_OqKrTq4riZiWMd'
    )

    stripe.PaymentIntent.capture(
        payment.id,
    )


    print(payment)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
