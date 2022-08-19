import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():
    link = stripe.PaymentLink.modify(
        "plink_1LQfcKILwdSSnvJbxIylZ276",
        line_items=[
            {
                id:'price_1KUgoCILwdSSnvJbHcrS5qHd'
            }
        ],
    )

    print(link)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
