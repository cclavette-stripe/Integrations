import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def transfer():
    return stripe.Transfer.create(
        amount=400,
        currency="usd",
        destination="acct_1L0ajSRAzYcRRMwc",
)


def main():
    # testing Stripe instance properly configured
    print(transfer())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    