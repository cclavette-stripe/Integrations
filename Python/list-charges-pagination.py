import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = '2017-08-15'

# DEFINE FUNCTIONS
def list_charges():
    charges = stripe.Charge.list(
            created= {'gt': 1623708795}, limit=100, expand=["data.customer"]
    )
    d =0
    for i in charges.data:
        print(str(d) + ':' + i.id)
        d = d+1

def main():
    # testing Stripe instance properly configured
    list_charges()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    