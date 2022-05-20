import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def create_customer():
    return stripe.Customer.create(
        name='Count Bouregard'
    )

new_cus = create_customer()

def attach_pm():    
    return stripe.PaymentMethod.attach(
        "pm_card_visa",
        customer=new_cus.id,
    )

new_pm = attach_pm()

def update_customer():
    return stripe.Customer.modify(
        new_cus.id,
        invoice_settings= {
            "default_payment_method": new_pm.id
        }
    )


def main():
    # testing Stripe instance properly configured
    print(update_customer())

    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    