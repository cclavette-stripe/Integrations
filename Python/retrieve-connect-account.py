import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = 'sk_test_51E7YoAILwdSSnvJbqveJLUBlaW70f9QLaGWzliYl0rHaNEUed7U0ufabQO5cFT2S536SMA6i22OpRenFhvaJ7wRs00z1gnajW2'

# DEFINE FUNCTIONS
def test():

    acct = stripe.Account.retrieve("acct_1KbCDrRNufchDxGg")
    print(acct)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    