import stripe
import os
from dotenv import load_dotenv
import time

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

test_clock = object()
customer = object()

# DEFINE FUNCTIONS
def create_test_clock():
    return stripe.test_helpers.TestClock.create(
        ## This gets a unix timestamp for exactly 24 hours after the time of the function call
        frozen_time=int(time.time() + 86400),
        name="Test clock (starts tomorrow)",
)

def create_customer(clock_id):
    return stripe.Customer.create(
        email="test@clock.com",
        test_clock=clock_id,
        payment_method="pm_card_visa",
        invoice_settings={"default_payment_method": "pm_card_visa"},
    )

def main():
    test_clock = create_test_clock()
    customer = create_customer(test_clock.id)
    print(customer.id, test_clock.id)
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    