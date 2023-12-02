from ast import Subscript
from tkinter import N
import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
new_product = object()
new_price1 = 'price_1Kw9ZWILwdSSnvJb3g6CS0sX'
new_price2 = 'price_1KvoxhILwdSSnvJbGSBsYCIk'
new_customer = object()
new_invoice = object()
new_pm = object()
new_sub = object()


def create_product():
    return stripe.Product.create(name="Monthly recurring")

def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 5,
            "exp_year": 2025,
            "cvc": "314",
        },
    )

def create_customer(name, pm):
    return stripe.Customer.create(
        name=name,
        payment_method=pm
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

def create_sub(cus_id, price1, price2):
    return stripe.Subscription.create(
    customer=cus_id,
    trial_end=1701499029,
    items=[
        {
        "price": price1,
        },
    ],
    # add_invoice_items=[
    #     {
    #     "price": price2,
    #     }
    # ]
)

def create_ii(cus_id, price, sub_id):
    return stripe.InvoiceItem.create(
        customer=cus_id,
        price=price,
        subscription=sub_id,
)

def main():
    new_pm = create_pm()
    new_customer = create_customer('Clock Test', new_pm)
    attach_pm(new_customer.id, new_pm.id)
    update_customer(new_customer.id, new_pm.id)
    new_product = create_product()
    new_sub = create_sub(new_customer.id, new_price1, new_price2)
    create_ii(new_customer, new_price2, new_sub.id)
    print(new_sub.id)

    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    