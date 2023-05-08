from ast import Subscript
from tkinter import N
import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def create_product():
    return stripe.Product.create(name="Gold Special")


def create_price():
    return stripe.Price.create(
        product=create_product().id,
        unit_amount=111000,
        currency="usd",
    )


def create_customer():
    return stripe.Customer.create(
        name="Some Guy"
    )


new_customer = create_customer()


def create_invoice_item():
    return stripe.InvoiceItem.create(
        customer=new_customer.id,
        price=create_price().id,
    )


def create_invoice(pm):
    invoice = stripe.Invoice.create(
        customer=new_customer.id,
        default_payment_method=pm,
        expand=['payment_intent']
    )

    return invoice


def create_pm():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 8,
            "exp_year": 2024,
            "cvc": "314",
        },
    )


def attach_pm(cus, pm):
    stripe.PaymentMethod.attach(
        pm,
        customer=cus,
    )


def update_pi(pi, pm):
    return stripe.PaymentIntent.modify(
        pi,
        payment_method=pm
    )


def finalize_invoice(inv):
    return stripe.Invoice.finalize_invoice(
        inv,
    )


def pay_invoice(id):
    return stripe.Invoice.pay(
        id,
    )


def main():
    # testing Stripe instance properly configured
    create_invoice_item()
    new_pm1 = create_pm()
    new_pm2 = create_pm()
    attach_pm(new_customer.id, new_pm1.id)
    attach_pm(new_customer.id, new_pm2.id)
    new_inv = create_invoice(new_pm1.id)
    finalize_invoice(new_inv.id)
    print(new_inv)
    print(new_pm2)
    update_pi(new_inv.payment_intent, new_pm2.id)


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
