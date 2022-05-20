const stripe = require('stripe')('sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib');
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-connect-customer', async (req, res) => {
    const customer = await stripe.customers.create(
        {email: 'person@example.edu'},
        {stripeAccount: 'acct_1KqOHIDLXCJQbu9g'}
      );
      
      // Fetching an account just needs the ID as a parameter
      const account = await stripe.accounts.retrieve('acct_1KqOHIDLXCJQbu9g');
      console.log(account);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});