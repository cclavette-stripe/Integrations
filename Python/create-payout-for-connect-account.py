import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def payout():
    payout = stripe.Payout.create(
        amount=1100, 
        currency="usd",
        stripe_account="acct_1L0ajSRAzYcRRMwc"
        )
    print(payout)


def main():
    # testing Stripe instance properly configured
    payout()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    