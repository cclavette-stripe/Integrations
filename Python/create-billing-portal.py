import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def billing_port():
    config = stripe.billing_portal.Configuration.create(
        business_profile={
            "headline": "Customer portal via the API!",
        },
        features={
            "invoice_history": {"enabled": True},
            "subscription_cancel": {"enabled": True, "mode": "immediately"},
            "customer_update": {
                "enabled": True,
                "allowed_updates": ["name", "email", "address", "shipping", "phone", "tax_id"]
                },
            "payment_method_update": {"enabled": True},
            "subscription_update": {
                "enabled": True,
                "default_allowed_updates": ["price", "quantity", "promotion_code"],
                "products": [
                    {
                        "product": "prod_MqjJntpSKFnMrP",
                        "prices": ["price_1MMJO1ILwdSSnvJbj3DhGODZ", "price_1MMJNoILwdSSnvJbH73xRFYy"]
                    }
                ],
            },
        },
    )

    return stripe.billing_portal.Session.create(
        customer="cus_Mb4GHVTViPWn1j",
        return_url="https://example.com/account",
        configuration=config.id
    )


def main():
    # testing Stripe instance properly configured
    print(billing_port())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
