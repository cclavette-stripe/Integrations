from ast import Subscript
from tkinter import N
import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
new_product = object()
new_price = object()
new_customer = object()
new_invoice = object()
new_pm = object()


def create_product():
    return stripe.Product.create(name="Gold Special")


def create_price(prod_id):
    return stripe.Price.create(
        product=prod_id,
        unit_amount=111000,
        currency="usd",
    )


def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 5,
            "exp_year": 2023,
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


def create_invoice_item(cus_id, price_id):
    return stripe.InvoiceItem.create(
        customer=cus_id,
        price=price_id,
    )


def attach_pm(cus_id, pm):
    return stripe.PaymentMethod.attach(
        pm,
        customer=cus_id,
    )


def create_invoice(cus_id):
    return stripe.Invoice.create(
        customer=cus_id,
        auto_advance="false"
    )


def update_invoice(invoice_id):
    return stripe.Invoice.modify(
        invoice_id,
        metadata={"order_id": "6735"},
    )


def pay_invoice(inv_id):
    return stripe.Invoice.pay(inv_id)


def main():
    new_pm = create_pm()
    new_customer = create_customer('Hans Zimmer', new_pm)
    attach_pm(new_customer.id, new_pm.id)
    update_customer(new_customer.id, new_pm.id)
    new_product = create_product()
    new_price = create_price(new_product.id)
    create_invoice_item(new_customer.id, new_price.id)
    new_invoice = create_invoice(new_customer.id)
    update_invoice(new_invoice.id)
    print(pay_invoice(new_invoice))


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
