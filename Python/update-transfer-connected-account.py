import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():

    # payment = stripe.PaymentIntent.modify(
    #     "py_1LNKMvRAzYcRRMwc6NJdtfRo",
    #     metadata={"order_id": "6735"},
    #     stripe_account='acct_1E7YoAILwdSSnvJb',
    # )

    transfer = stripe.Transfer.modify(
        "py_1MS2n5RNufchDxGgx0ugPX6P",
        metadata={"order_id": "6735"}
    )

    print(transfer)


def main():
    # testing Stripe instance properly configured
    print(test())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
