import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

card = stripe.Token.create(
  card={
    "number": "4242424242424242",
    "exp_month": 11,
    "exp_year": 2024,
    "cvc": "314",
  },
)

customer = stripe.Customer.create(
  description="MOTO customer",
  source= card.id
)

si = stripe.SetupIntent.create(
  # usage= "off_session",
  confirm= "True",
  customer= customer,
  payment_method= card.card.id,
  payment_method_types= {
    0: "card",
  },
  payment_method_options= {
    "card": {
      "moto": "True",
    },
  }
)

pi = stripe.PaymentIntent.create(
  currency= "cad",
  customer= customer.id,
  off_session= "True",
  payment_method= card.card.id,
  on_behalf_of= "acct_1KbCDrRNufchDxGg",
  confirm= "True",
  amount= "25000",
  payment_method_types= {
    0: "card",
  },
)

print(pi)