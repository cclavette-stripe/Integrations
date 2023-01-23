from ast import Subscript
from tkinter import N
import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
new_product = object()
new_price = object()
new_customer = object()
new_invoice = object()
new_pm = object()
new_sub = object()


def create_product():
    return stripe.Product.create(name="Monthly recurring")

def create_price(prod_id):
    return stripe.Price.create(
        product=prod_id,
        unit_amount=1,
        nickname='Monthly recurring price',
        recurring={
            "interval": "month"
        },
        currency="usd",
    )

def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4000001240000000",
            "exp_month": 5,
            "exp_year": 2023,
            "cvc": "314",
        },
    )

def retrieve_customer(name, pm):
    return stripe.Customer.retrieve("cus_N95FjHGA4a7AgR")


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

def create_sub(cus_id, price_id):
    return stripe.Subscription.create(
    customer=cus_id,
    currency='CAD',
    items=[
        {
        "price": price_id,
        },
    ],
    )

def main():
    new_pm = create_pm()
    new_customer = retrieve_customer('Harry Style', new_pm)
    attach_pm(new_customer.id, new_pm.id)
    update_customer(new_customer.id, new_pm.id)
    new_product = create_product()
    new_price = create_price(new_product.id)
    new_sub = create_sub(new_customer.id, new_price.id)
    print(new_sub)

    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    