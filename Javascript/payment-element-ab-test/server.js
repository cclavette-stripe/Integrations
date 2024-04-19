const express = require("express");
const app = express();

// This is your test secret API key.
const stripe = require('stripe')("sk_test_51Of6ruKJvCEJVBeZ5ZJrWcXshuTBjJIbt6t0ygoFxvj2EM7jyXILdFCenqZiLcJdzSQNkvkgdUKKqPIrcFAMqJBH00uS4x2MqT");

app.use(express.static("."));
app.use(express.json());

app.post("/create-payment-intent", async (req, res) => {
  const { items } = req.body;

  // Create a PaymentIntent with the order amount and currency
  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1499,
    // payment_method_types: [
    //   "card",
    // ],
    automatic_payment_methods: {
      enabled: true,
    },
    // capture_method: "manual",
    // setup_future_usage: "off_session",
    currency: "usd",
    // payment_method_configuration: 'pmc_1OhOmzKJvCEJVBeZcM0jmM22',
    
  });

  res.send({
    clientSecret: paymentIntent.client_secret,
  });
});

app.listen(4242, () => console.log("Node server listening on port 4242!"));