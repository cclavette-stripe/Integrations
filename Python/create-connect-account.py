import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def create_account():

    account = stripe.Account.create(
        type="custom",
        email="seedfoundry.dev@gmail.com"
    )

    print(account)


def main():
    # testing Stripe instance properly configured
    create_account()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    