const express = require("express");
const app = express();

// This is your test secret API key.
const stripe = require('stripe')("sk_test_51OeizIFsHUo8ra70UhZsfuC8EyT8aFeFYEUDF8VQWWF2ROyIFbmObtFTgEWv1uKSsweIfJOf1jjZ72097nqdR72a00wRJjzOe3");

app.use(express.static("."));
app.use(express.json());

const calculateOrderAmount = (items) => {
  // Replace this constant with a calculation of the order's amount
  // Calculate the order total on the server to prevent
  // people from directly manipulating the amount on the client
  return 1400;
};

app.post("/create-payment-intent", async (req, res) => {
  const { items } = req.body;

  // Create a PaymentIntent with the order amount and currency
  const paymentIntent = await stripe.paymentIntents.create({
    amount: calculateOrderAmount(items),
    // payment_method_types: [
    //   "card",
    // ],
    automatic_payment_methods: {
      enabled: true,
    },
    // capture_method: "manual",
    // setup_future_usage: "off_session",
    currency: "gbp",
    
  });

  res.send({
    clientSecret: paymentIntent.client_secret,
  });
});

app.listen(3000, () => console.log("Node server listening on port 3000!"));