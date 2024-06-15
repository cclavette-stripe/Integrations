import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = '2018-10-31'


# DEFINE FUNCTIONS
def test():

    prod = stripe.Price.retrieve("price_1PHDPjILwdSSnvJbsegzPBX3", expand=["currency_options"])

    print(prod)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    