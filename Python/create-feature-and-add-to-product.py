import stripe
import os
import random
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS
def test():
    ran_num = random.randint(1, 10000)
    feature = stripe.entitlements.Feature.create(
        name="Some new feature: " + str(ran_num),
        lookup_key=ran_num,
        metadata= {
            "key": "value"
        }
    )
    product = stripe.Product.create(name="Product with entitlement and feature")

    add_to_product = stripe.Product.create_feature(
        product.id,
        entitlement_feature=feature.id,
    )

    print(add_to_product)


def main():
    # testing Stripe instance properly configured
    test()
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    