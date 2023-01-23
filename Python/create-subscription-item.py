import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def create_item():
    new_item = stripe.SubscriptionItem.create(
        subscription="sub_1Lrs7fILwdSSnvJbgUvNMOG4",
        price="price_1MF3hIILwdSSnvJboONkJYon",
        quantity=2,
    )

    print(new_item)


def main():
    create_item()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
