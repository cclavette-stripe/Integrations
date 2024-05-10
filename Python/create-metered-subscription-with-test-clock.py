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
meter = object()
ran_num = str(random.randrange(1, 10000))

# DEFINE FUNCTIONS
def create_meter(ran_num):
    return stripe.billing.Meter.create(
        display_name="Meter Name: " + ran_num,
        event_name="event_name_" + ran_num,
        default_aggregation={"formula": "sum"},
        customer_mapping={"event_payload_key": "stripe_customer_id", "type": "by_id"},
        value_settings={"event_payload_key": "api_requests"},
    )

def create_price(id, ran_num):
    return stripe.Price.create(
        currency="usd",
        unit_amount=4,
        billing_scheme="per_unit",
        transform_quantity={"divide_by": 1000, "round": "up"},
        recurring={"usage_type": "metered", "interval": "month", "meter": id},
        product_data={"name": "Product Name: " + ran_num},
    )

def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            # Test card for failed payment after successfull attach
            "number": "4000000000000341",
            "exp_month": 5,
            "exp_year": 2030,
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
        expand=["pending_setup_intent"]
    )


def create_meter_event(cus_id, ran_num):
    return stripe.billing.MeterEvent.create(
        event_name="event_name_" + ran_num,
        payload={"api_requests": "123456789012345678901234597890123456789", "stripe_customer_id": cus_id},
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
    pm = create_pm()
    clock = create_test_clock()
    customer = create_customer('Clock Test' + ran_num, pm, clock.id)
    attach_pm(customer.id, pm.id)
    update_customer(customer.id, pm.id)
    meter = create_meter(ran_num)
    price = create_price(meter.id, ran_num)
    sub = create_sub(customer.id, price.id)
    # create_ii(customer, price2, sub.id)
    print(create_meter_event(customer.id, ran_num))
    # print(sub["items"]["data"][0]["id"])
    # print(json.dumps(sub))
    advance_clock(clock.id)
    print(sub.id)


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
