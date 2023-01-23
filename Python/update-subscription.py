import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY
new_item = create_item()


# DEFINE FUNCTIONS


def change_sub():
    sub = stripe.Subscription.modify(
        "sub_1Lrs7fILwdSSnvJbgUvNMOG4",
        metadata={"order_id": "6735"},
        proration_behavior='invoice_immediately',
        # trial_end=1668549252
        # billing_cycle_anchor= 1659807119,
        items = [{
            "id": "si_LncGW32Pki9eDv",
            'quantity': 2
        }],
    )

    print(sub)


def main():
    change_sub()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
