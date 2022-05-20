import stripe
import os
from dotenv import load_dotenv

load_dotenv() # load .env defined environment 
stripe.api_key = 'rk_test_51E7YoAILwdSSnvJbgTNEEBVdVr5jAZa2s3H3kGH4qApSLoM6DbS7l6rSOXHsFTDifTG5fYgbZqzPqaer3825ERTx001eltMvA3'

# DEFINE FUNCTIONS
def get_report():
    return stripe.reporting.ReportType.retrieve('balance.summary.1')


def main():
    # testing Stripe instance properly configured
    print(get_report())
    
    
if __name__ == "__main__":
    # This will run if this file is invoked from the command line
    main()
    
    