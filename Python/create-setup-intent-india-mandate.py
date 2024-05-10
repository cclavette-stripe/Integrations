import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def test():
    new_customer = stripe.Customer.create(
        description="India setup intent payment guy",
    )

    new_pm = stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4000002760003184",
            "exp_month": 8,
            "exp_year": 2029,
            "cvc": "314",
        },
    )

    print(stripe.PaymentMethod.attach(
        new_pm,
        customer=new_customer,
    ))

    setup_intent = stripe.SetupIntent.create(
        customer=new_customer,
        payment_method=new_pm,
        confirm=True,
        return_url='https://example.com/success',
        payment_method_options={
            'card': {
                'mandate_options': {
                    'reference': 'Some reference number 12398234982',
                    'description': 'Dome description',
                    'amount': '4555',
                    'currency': 'inr',
                    'amount_type': 'maximum',
                    'start_date': '1671050177',
                    'end_date': '1671140177',
                    'interval': 'week',
                    'interval_count': '1',
                    'supported_types': ['india']
                }
            }
        },
    )
    print(setup_intent)

    stripe.SetupIntent.confirm(
        setup_intent.id,
        return_url='https://example.com/success',
    )


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
