const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-payment-intent', async (req, res) => {
    const invoice = await stripe.invoices.retrieveUpcoming({
        customer: 'cus_O0dIMQlVzahoPr',
        subscription: 'sub_1NkvcVILwdSSnvJbCtu2MQEo',
        subscription_items: [{
            id: 'si_OY1heVRyfO89pi',
            price: 'price_1NyISZILwdSSnvJbuDjALFmV'
        }]
      });

      console.log(invoice);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});