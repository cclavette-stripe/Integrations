import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('ISSUING_SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test():
  card = stripe.issuing.Card.create(
     
    stripe_account='acct_1NioLSPZANSIMssh',

    cardholder="ich_1Niov1PZANSIMssh9lZRRKMP",
    currency="gbp",
    type="virtual",
  )

  print(card)

def main():
    # testing Stripe instance properly configured
    test()
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    