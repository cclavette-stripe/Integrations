import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

print(stripe.PaymentIntent.create(
    customer='cus_LVGarIyHMOvvs6',
    confirm=True,
    payment_method='pm_1KoG3KILwdSSnvJbxdZ6S2nZ',
    amount=2000,
    currency="usd",
    payment_method_types=["card"],
    expand=['customer']
))
