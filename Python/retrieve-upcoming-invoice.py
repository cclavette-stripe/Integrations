import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def get_invoice():
    inv = stripe.Invoice.upcoming(
        customer ='cus_LHpPV1qTGsDbdj',
        subscription ='sub_1Kz5dIILwdSSnvJbGLQg7bwE',
        ##subscription_proration_behavior = 'always_invoice',
        ##subscription_billing_cycle_anchor = 'unchanged',
        ##subscription_trial_end = 'now',
        # subscription_proration_date=1652501042,
        subscription_items = [{
            'id': 'si_LgSYRxuUN781q2',
            'quantity': 100
        }],
    )

    print(inv)

def main():
    # testing Stripe instance properly configured
    get_invoice()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    