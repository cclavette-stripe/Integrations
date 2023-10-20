import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY
# stripe.api_version = "2018-02-28"

# DEFINE FUNCTIONS


def test():

    session = stripe.checkout.Session.create(
        line_items=[{
            'price': 'price_1Me05gILwdSSnvJbBRI5m5dt',
            'quantity': 1
        }],
        mode='payment',
        customer='cus_OY2Zs60c0PSEv0',
        # allow_promotion_codes=True,
        # payment_method_options={
        #     "us_bank_account": {
        #         "financial_connections" : {
        #             "permissions" : ["payment_method"]
        #         }
        #     }
        # },
        success_url='https://example.com/success',
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
