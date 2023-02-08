const stripe = require("stripe")(process.env.SEC_KEY);
const express = require('express');
const app = express();
app.use(express.static("."));

app.post('/create-intent', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: 'usd',
    automatic_payment_methods: {enabled: true},
  });
  res.json({client_secret: intent.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});