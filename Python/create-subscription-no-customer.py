import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
new_product = object()
new_price = object()
new_invoice = object()
new_pm = object()
new_sub = object()


def create_product():
    return stripe.Product.create(name="Monthly recurring")

def create_price(prod_id):
    return stripe.Price.create(
        product=prod_id,
        unit_amount=10000,
        nickname='Monthly recurring price',
        recurring={
            "interval": "month"
        },
        currency="usd",
    )





def create_sub(price_id):
    return stripe.Subscription.create(
    pay_immediately=False,
    # off_session=False,
    items=[
        {
        "price": price_id,
        },
    ],
    )

def main():
    new_product = create_product()
    new_price = create_price(new_product.id)
    new_sub = create_sub( new_price.id)
    print(new_sub)

    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    