import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def refund():
    stripe.Refund.create(
    charge="py_1MS2n5RNufchDxGgx0ugPX6P",
    amount=3100,
    # payment_intent='pi_3NJftuILwdSSnvJb1FCr0LEh',
    reverse_transfer=True
)


def main():
    # testing Stripe instance properly configured
    refund()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    