import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def change_sub():
    sub = stripe.Subscription.modify(
        "sub_1L611iILwdSSnvJbRSSIjEob",
        proration_behavior='none',
        items = [{
            "id": "si_LncGW32Pki9eDv",
            'quantity': 2
        }],
)

    print(sub)

def main():
    # testing Stripe instance properly configured
    change_sub()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    