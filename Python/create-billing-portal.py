import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def billing_port():
    # return stripe.billing_portal.Configuration.create(
    #     business_profile={
    #         "headline": "Customer portal via the API!",
    #             },
    #         features={"invoice_history": {"enabled": True}},
    #     )
    return stripe.billing_portal.Session.create(
        customer="cus_EiZOLZ4ZPiejyu",
        return_url="https://example.com/account",
    )


def main():
    # testing Stripe instance properly configured
    print(billing_port())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
