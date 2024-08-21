import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def get_bt():
    return stripe.BalanceTransaction.list(
        source="ch_3PXtHyILwdSSnvJb01K84Htd"
    )


def main():
    # testing Stripe instance properly configured
    print(get_bt())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    