const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

num = Math.round((10.8899 + Number.EPSILON) * 100) 

app.post('/create-payment-intent', async (req, res) => {
    const paymentIntent = await stripe.paymentIntents.create({
        amount: num,
        currency: 'usd',
        capture_method: 'automatic',
        automatic_payment_methods: {
            enabled: true,
        },
    });
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});