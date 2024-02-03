import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY
stripe.api_version = '2020-08-27'


# DEFINE FUNCTIONS


def change_sub():
    sub = stripe.Subscription.modify(
        "sub_1OIbxrILwdSSnvJbBI45LPSu",
        # metadata={"order_id": "6735"},
        proration_behavior='always_invoice',
        # pay_immediately=False,
        items = [{
            "price": 'price_1OPYndILwdSSnvJbOT1tGTnZ'
        }],
        # promotion_code='promo_1OHEmYILwdSSnvJbty4pu8oo'
        # # trial_end=1668549252
        billing_cycle_anchor= 'now',
        # items = [{
        #     "id": "si_LncGW32Pki9eDv",
        #     'quantity': 2
        # }],
    )

    print(sub)


def main():
    change_sub()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
