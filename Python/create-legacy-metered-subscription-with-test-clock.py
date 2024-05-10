from ast import Subscript
from tkinter import N
import stripe
import os
import time
from dotenv import load_dotenv
import json

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
new_product = object()
new_price = 'price_1MyHylILwdSSnvJbYy6H9CDm'
new_customer = object()
new_invoice = object()
new_pm = object()
new_sub = object()
new_clock = object()


def create_product():
    return stripe.Product.create(name="Monthly recurring",)


def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            # Test card for failed payment after successfull attach
            "number": "4000000000000341",
            "exp_month": 5,
            "exp_year": 2023,
            "cvc": "314",
        },
    )


def create_test_clock():
    return stripe.test_helpers.TestClock.create(
        frozen_time=int(time.time()),
    )


def create_customer(name, pm, clock):
    return stripe.Customer.create(
        name=name,
        payment_method=pm,
        test_clock=clock
    )


def update_customer(cus_id, pm):
    return stripe.Customer.modify(
        cus_id,
        invoice_settings={
            "default_payment_method": pm
        }
    )


def attach_pm(cus_id, pm):
    return stripe.PaymentMethod.attach(
        pm,
        customer=cus_id,
    )


def create_sub(cus_id, price):
    return stripe.Subscription.create(
        customer=cus_id,
        collection_method='charge_automatically',
        payment_behavior='default_incomplete',
        # The below timestamp is 24 hours (e.g. 86400 seconds) in the future
        # trial_end=int(time.time()) + 86400,
        items=[
            {
                "price": price,
            },
        ],
    )


def update_usage(sub_item):
    return stripe.SubscriptionItem.create_usage_record(
        sub_item,
        quantity=100,
        timestamp='now',
        action='set'
    )


def advance_clock(id):
    stripe.test_helpers.TestClock.advance(
        id,
        # The below timestamp is 25 hours and 10 minutes (e.g. 90600 seconds) in the future (an hour is added to finalize the new invoice)
        frozen_time=int(time.time() + 90600),
    )


# def create_ii(cus_id, price, sub_id):
#     return stripe.InvoiceItem.create(
#         customer=cus_id,
#         price=price,
#         subscription=sub_id,
#     )


def main():
    new_pm = create_pm()
    new_clock = create_test_clock()
    new_customer = create_customer('Clock Test', new_pm, new_clock.id)
    attach_pm(new_customer.id, new_pm.id)
    update_customer(new_customer.id, new_pm.id)
    new_product = create_product()
    new_sub = create_sub(new_customer.id, new_price)
    # create_ii(new_customer, new_price2, new_sub.id)
    update_usage(new_sub["items"]["data"][0]["id"])
    # print(new_sub["items"]["data"][0]["id"])
    # print(json.dumps(new_sub))
    advance_clock(new_clock.id)
    print(new_sub.id)


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
