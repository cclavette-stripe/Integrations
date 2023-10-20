import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('ISSUING_SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test():
  cardholder = stripe.issuing.Cardholder.create(
    # REMOVE ME IF ERRORS OCCUR
    stripe_account='acct_1NioLSPZANSIMssh',

    name="Jenny Rosen",
    email="jenny.rosen@example.com",
    phone_number="+18008675309",
    status="active",
    type="individual",
    individual={
      "first_name": "Jenny",
      "last_name": "Rosen",
      "dob": {"day": 1, "month": 11, "year": 1981},
  },
  billing = {
    "address": {
      "line1": "49 Featherstone Street",
      "city": "LONDON",
      "postal_code": "EC1Y 8SY",
      "country": "GB",
    },
  },
)

  print(cardholder)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    