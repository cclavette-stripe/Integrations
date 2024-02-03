import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = '2018-10-31'

# DEFINE FUNCTIONS
def list_prods():
    prod = stripe.Price.list()
    print(prod)
    # for i in prod.data:
    #     print(i.id)

def main():
    # testing Stripe instance properly configured
    list_prods()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    