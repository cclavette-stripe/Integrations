import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def update_account():
    account = stripe.Account.modify(
        "acct_1MPDuvRHXEj5KAaO",
        # settings={"payments": {"statement_descriptor": ""}}
        # tos_acceptance={"date": 1609798905, "ip": "8.8.8.8"},
        capabilities={
            "card_payments" : {
                "requested": True
            },
            "wechat_pay_payments" : {
                "requested": True
            }
        }

    )
    print(account)


def main():
    # testing Stripe instance properly configured
    update_account()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
