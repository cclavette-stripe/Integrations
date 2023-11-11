const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-payment-intent', async (req, res) => {
    const customer = await stripe.customers.create();

    const paymentIntent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: 'usd',
        customer: customer.id,
    });

    res.send({ clientSecret: paymentIntent.client_secret });
});


app.listen(3000, () => {
    console.log('Running on port 3000');
});