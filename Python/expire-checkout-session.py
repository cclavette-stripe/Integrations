import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test():
    cs = stripe.checkout.Session.expire(
  "cs_test_a180oxmgkoEYhrnmLSWR60xI6yVQ0r4s3tPBdTZxHMLr5kEQvaRg5vS38x",
)
    print(cs)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    