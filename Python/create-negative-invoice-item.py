from ast import Subscript
from tkinter import N
import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
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
        amount= -122,
        currency= "usd",
        invoice='in_1Me0A5ILwdSSnvJbhbH9PPha'
    )

def create_invoice():
    return stripe.Invoice.create(
        customer=new_customer.id,
        expand=['payment_intent']
    )

def main():
    # testing Stripe instance properly configured
    create_invoice_item()
    print(create_invoice())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    