import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


# def create_pm():
#     return stripe.PaymentMethod.create(
#         type="card",
#         card={
#             "number": "4242424242424242",
#             "exp_month": 8,
#             "exp_year": 2023,
#             "cvc": "314",
#         },
#     )


def test():
    setup_intent = stripe.SetupIntent.create(
        # payment_method=id,
        # customer="cus_MP1RJAj7YHk6PL",
        payment_method_options={"card"},
        # confirm=True,
    )
    print(setup_intent)


def main():
    # testing Stripe instance properly configured
    test()


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
