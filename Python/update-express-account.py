import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def update_account():
    account = stripe.Account.modify(
        "acct_1032D82eZvKYlo2C",
        metadata={"order_id": "6735"}
    )
    print(account)


def main():
    # testing Stripe instance properly configured
    print(update_account())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    