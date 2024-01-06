import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def update_account():

    account = stripe.Account.modify_capability(
        "acct_1MPDuvRHXEj5KAaO",
        "legacy_payments",
        requested=False,
    )
    print(account)


def main():
    # testing Stripe instance properly configured
    update_account()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
