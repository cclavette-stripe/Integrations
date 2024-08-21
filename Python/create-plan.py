import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test():

    balance = stripe.Plan.create(
  amount=1200,
  currency="usd",
  interval="month",
  product="prod_PyRzre6pyGRDvB",
  trial_period_days=0
)
    print(balance)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    