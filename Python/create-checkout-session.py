import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = 'sk_test_51PQu7jAdjRHH0avyHQvgBnVY7HkchvmKFeEmlpwL4OY0p8r87oPoCeJFC9sBf1ibveBViEuJxm1FUtGKjLMXvhIj00NM35b5CP'
stripe.api_key = STRIPE_SECRET_KEY
# stripe.api_version = "2018-02-28"

# DEFINE FUNCTIONS


def test():

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': "sek",
                'product_data': {
                    'name': "Test Event - Jesper Jacobsen",
                },
                # 'tax_behavior': "inclusive",
                'unit_amount': "2800",
            },
            'quantity': 1,
        }],
        mode='payment',
        # customer='cus_OY2Zs60c0PSEv0',
        # allow_promotion_codes=True,
        payment_method_types= ['card', 'swish'],
        payment_method_options={
            'swish': {
                'reference': '1234567890',
            }
        #     "us_bank_account": {
        #         "financial_connections" : {
        #             "permissions" : ["payment_method"]
        #         }
        #     }
        },
        success_url='http://localhost:4242/checkout.html',
        cancel_url='https://example.com/cancel',
        # idempotency_key='u6rjmgMlligPRlUf'
    )
    print(session)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
