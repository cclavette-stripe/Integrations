import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def update_customer():
    return stripe.Customer.modify(
        "cus_NKIHc8dS2esHgP",
        shipping={
            "name": "Curry Clerk",
            "address": {
                "city": "",
                "country": "",
                "line1": "",
                "postal_code": "",
                "state": ""
            },

        }
    )


def main():
    # testing Stripe instance properly configured
    print(update_customer())

    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    