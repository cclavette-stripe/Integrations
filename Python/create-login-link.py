import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY


def create_account():
    acct = stripe.Account.create(
        type='standard',
        email="jenny@example.com",
    ),
    company = {
        "phone": 5416038514
    }
    return(acct)

# DEFINE FUNCTIONS


def login_link():
    acct = create_account()
    print(acct)
    link = stripe.AccountLink.create(
        account=acct.id,
        type='account_onboarding',
        return_url='https://www.someurl.com',
        refresh_url="https://www.someurl.com"
    )
    return(link)


def main():
    # testing Stripe instance properly configured
    print(login_link())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
