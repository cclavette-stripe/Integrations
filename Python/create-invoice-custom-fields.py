from ast import Subscript
import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def custom_fields():
    stripe.Invoice.create(
        customer="cus_LHpPV1qTGsDbdj",
        due_date=1705820577
        # subscription="sub_1KbFkfILwdSSnvJbdLWVsJeb",
        # custom_fields=
        #     [
        #         {"name": "key1", "value": "value1"},
        #         {"name": "key2", "value": "value2"}
        #     ]
    )


def main():
    # testing Stripe instance properly configured
    custom_fields()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    