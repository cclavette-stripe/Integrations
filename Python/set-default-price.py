import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test_balance():
    stripe.Product.modify(
    "prod_LB2uHJZAzMcOtL",
    default_price= "price_1KUgoCILwdSSnvJbHcrS5qHd"
)

def main():
    # testing Stripe instance properly configured
    test_balance()
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    