const stripe = require('stripe')('sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib');
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-payment-intent', async (req, res) => {
    const paymentIntent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: 'usd',
        capture_method: 'automatic',
        automatic_payment_methods: {
            enabled: true,
        },
        payment_method: 'pm_1Klm13ILwdSSnvJb423LderZ'
    });
});


app.listen(3000, () => {
    console.log('Running on port 3000');
});