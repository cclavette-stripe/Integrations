import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
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
                "proration_behavior": "always_invoice",
                "products": [
                    {
                        "product": "prod_QeLgrGL7wa2FTu",
                        "prices": ["price_1Pn2z8ILwdSSnvJb9pTqUS7F"]
                    },
                    {
                        "product": "prod_QPPY0Wy7Y81x1G",
                        "prices": ["price_1PYajVILwdSSnvJbt6hWHWd3"]
                    }
                ],
            },
        },
        login_page={
            "enabled": True,
        }
    )

    print(config)

    return stripe.billing_portal.Session.create(
        customer="cus_OY2Zs60c0PSEv0",
        return_url="https://example.com/account",
        configuration=config.id
    )


def main():
    # testing Stripe instance properly configured
    print(billing_port())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
