import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
STRIPE_SECRET_KEY = os.getenv('SEC_KEY')
stripe.api_key = STRIPE_SECRET_KEY

payment = stripe.PaymentIntent.create(
    customer='cus_LVGarIyHMOvvs6',
    confirm=True,
    payment_method='pm_1KoG3KILwdSSnvJbxdZ6S2nZ',
    amount=700000,
    currency="usd",
    payment_method_types=["card"],
    transfer_group='SOMETRANSFERGROUP',
    # transfer_data={
    #   'destination': 'acct_1KqOHIDLXCJQbu9g',
    # },
    on_behalf_of='acct_1KqOHIDLXCJQbu9g',
    # application_fee_amount=700000,
    description="this is a description",
    expand=['charges']
)
print(payment)

# transfer_group = payment.transfer_group
# source_transaction = payment.charges.data[0].id

transfer = stripe.Transfer.create(
  amount=4000,
  currency="usd",
  destination="acct_1KqOHIDLXCJQbu9g",
  transfer_group='SOMETRANSFERGROUP',
  # source_transaction=source_transaction,
)

# print(transfer)