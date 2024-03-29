import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # load .env defined environment
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

# DEFINE FUNCTIONS


def transfer():
    return stripe.Transfer.create(
        amount=100000,
        currency="usd",
        source_transaction="ch_3MTZI3ILwdSSnvJb1OhX1b9J",
        destination="acct_1KbCDrRNufchDxGg",
    )


def main():
    # testing Stripe instance properly configured
    print(transfer())


if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
