from cgi import test
from re import sub
import stripe
import os
from dotenv import load_dotenv
import time

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

unix_today = int(time.time())
test_clock = object()
customer = object()
subscription = object()
invoice_item = object()

# DEFINE FUNCTIONS
def create_test_clock():
    return stripe.test_helpers.TestClock.create(
        ## This gets a unix timestamp for exactly 24 hours after the current day
        frozen_time=unix_today + 86400,
        name='Test clock (starts tomorrow)'
    )   

def create_customer(clock_id):
    return stripe.Customer.create(
        email='test@clock.com',
        test_clock=clock_id,
        payment_method='pm_card_visa',
        invoice_settings={'default_payment_method': 'pm_card_visa'}
    )

def create_sub(cus_id):
    return stripe.Subscription.create(
        customer=cus_id,
        trial_end=1653984468,
        items=[
            {
            'price': 'price_1Kw9ZWILwdSSnvJb3g6CS0sX',
            }
        ]
    )

def create_ii(cus_id, sub_id):
    return stripe.InvoiceItem.create(
        customer=cus_id,
        price='price_1KvoxhILwdSSnvJbGSBsYCIk',
        subscription=sub_id
    )

def advance_clock(clock_id):
    return stripe.test_helpers.TestClock.advance(
        clock_id, 
        ## Sets the time to 35 days from the current day
        frozen_time=int(unix_today + 3024000)
    )


def main():
    test_clock = create_test_clock()
    customer = create_customer(test_clock.id)
    subscription = create_sub(customer.id)
    invoice_item = create_ii(customer.id, subscription.id)
    advance_clock(test_clock.id)
    print(subscription.id)
    
if __name__ == '__main__':
    # This will run if this file is invoked from the command line
    main()
    
    