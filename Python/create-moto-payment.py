import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

print(stripe.PaymentIntent.create(
  amount=1099,
  currency="usd",
  return_url="https://www.google.com",
  customer="cus_MRGqlag0JKvfwM",
  payment_method="pm_1LiOJ1ILwdSSnvJbY9IRwNli",
  payment_method_options={"card": {"moto": True}},
  # automatic_payment_methods={"enabled": "true"},
  confirm=True
))
