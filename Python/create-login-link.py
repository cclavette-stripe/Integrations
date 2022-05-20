import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def login_link():
    link = stripe.Account.create_login_link(
        'acct_1KiPfsRCAojavCmH', 
        redirect_url='https://www.someurl.com'
    )
    print(link)


def main():
    # testing Stripe instance properly configured
    print(login_link())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    