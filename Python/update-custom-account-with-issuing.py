import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('ISSUING_SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def update_account():
    account = stripe.Account.modify(
        "acct_1Nio3MPg4uIJqOjQ",
        
        # capabilities={
        #     "transfers": {
        #         "requested": False
        #     },
        #     "card_issuing": {"requested": True},
        #     "us_bank_account_ach_payments": {"requested": True}
        # }
    )
    print(account)


def main():
    # testing Stripe instance properly configured
    print(update_account())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
