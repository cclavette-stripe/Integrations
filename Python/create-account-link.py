import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def login_link():
    link = stripe.AccountLink.create(
        account='acct_1NpDxYIHkLFrk61E',
        refresh_url="https://example.com/reauth",
        return_url="https://example.com/return",
        type="account_onboarding",
        collect="eventually_due",
    )
        
    return(link)


def main():
    # testing Stripe instance properly configured
    print(login_link())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    