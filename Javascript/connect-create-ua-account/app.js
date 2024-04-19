const stripe = require('stripe')(process.env.UA_SEC_KEY,
    {apiVersion: '2024-04-10; unified_accounts_beta=v1'});
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-ua-account', async (req, res) => {
    const account = await stripe.accounts.create({
        country: 'US',
      });

      console.log("THIS IS ON YOUR UA TEST ACCOUNT: ");
      console.log("Created account: " + account);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});