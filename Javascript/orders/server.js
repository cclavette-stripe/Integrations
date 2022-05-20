// This is a public sample test API key.
// Don’t submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
const stripe = require("stripe")("sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib", {
  apiVersion: "2020-08-27; orders_beta=v3",
});
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.use(express.static("."));

const validateItems = (items) => {
  // Replace this with any logic needed to validate product IDs
  // and quantities. For example: inventory checks.
  return true;
};

app.post("/create-order", bodyParser.json(), async (req, res) => {
  const { items } = req.body;

  if (!validateItems(items)) {
    res.status(400).send({ error: "Invalid items" });
  }

  const order = await stripe.orders.create({
    currency: "usd",
    line_items: items,
    payment: {
      settings: {
        payment_method_types: ["card"],
      },
    },
  });

  res.send({
    clientSecret: order.client_secret,
  });
});

app.listen(4242, () => console.log("Running on port 4242"));
