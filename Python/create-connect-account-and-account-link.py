import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
account_id = ''

def create_account():

    account = stripe.Account.create(
        country='US',
        type='standard',
        settings={'payouts': {'schedule': {'interval': 'manual'}}},
    )
    return(account.id)
    


def create_onboarding_link(acct):
    return stripe.AccountLink.create(
        account=acct,
        refresh_url="https://example.com/reauth",
        return_url="https://example.com/return",
        type="account_onboarding",
        collection_options= { 
            "fields": "eventually_due",
            "future_requirements": "include" 
        },
    )


def main():
    # testing Stripe instance properly configured
    account_id = create_account()
    print(create_onboarding_link(account_id))


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
