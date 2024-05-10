import stripe
import os
import time
from dotenv import load_dotenv
import json
import random

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE VARIABLES
price = object()
customer = object()
invoice = object()
pm = object()
sub = object()
clock = object()
ran_num = str(random.randrange(1, 10000))

# DEFINE FUNCTIONS
def create_price(ran_num):
    return stripe.Price.create(
        currency="usd",
        unit_amount=4000,
        recurring={"interval": "month", "interval_count": 1},
        product_data={"name": "Product Name: " + ran_num},
    )

# def create_pm():
#     return stripe.PaymentMethod.create(
#         type="card",
#         card={
#             # Test card for failed payment after successfull attach
#             "number": "4242424242424242",
#             "exp_month": 5,
#             "exp_year": 2030,
#             "cvc": "314",
#         },
#     )


def create_test_clock():
    return stripe.test_helpers.TestClock.create(
        frozen_time=int(time.time()),
    )


def create_customer(name, clock):
    return stripe.Customer.create(
        name=name,
        payment_method='pm_card_us',
        test_clock=clock
    )

def retrieve_pm(id):
    return stripe.PaymentMethod.list(
        customer=id,
    )


def update_customer(id, pm):
    return stripe.Customer.modify(
        id,
        invoice_settings={
            "default_payment_method": pm
        }
    )


def attach_pm(id, pm):
    return stripe.PaymentMethod.attach(
        pm,
        customer=id,
    )


def create_sub(cus_id, price_id):
    return stripe.Subscription.create(
        customer=cus_id,
        collection_method='charge_automatically',
        payment_behavior='default_incomplete',
        # The below timestamp is 24 hours (e.g. 86400 seconds) in the future
        # trial_end=int(time.time()) + 86400,
        items=[
            {
                "price": price_id,
            },
        ],
        discounts=[{"coupon": "50off4ever"}, {"coupon": "5E80ZjsS"}],
        # payment_settings={'save_default_payment_method': 'on_subscription'},
        expand=["pending_setup_intent"]
    )

def pay_invoice(id):
    return stripe.Invoice.pay(
        id,
        off_session=True
    )


def advance_clock(id):
    stripe.test_helpers.TestClock.advance(
        id,
        # The below timestamp is 25 hours and 10 minutes (e.g. 90600 seconds) in the future (an hour is added to finalize the new invoice)
        frozen_time=int(time.time() + 90600),
    )


def main():
    # pm = create_pm()
    clock = create_test_clock()
    customer = create_customer('Clock Test ' + ran_num, clock.id)
    pm = retrieve_pm(customer.id)
    attach_pm(customer.id, pm.data[0].id)
    update_customer(customer.id, pm.data[0].id)
    price = create_price(ran_num)
    sub = create_sub(customer.id, price.id)
    pay_invoice(sub.latest_invoice)
    advance_clock(clock.id)
    print(sub.id)


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
