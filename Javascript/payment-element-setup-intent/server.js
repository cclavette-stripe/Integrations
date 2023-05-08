const express = require("express");
const app = express();
// This is your test secret API key.
const stripe = require("stripe")(process.env.SEC_KEY, {
  apiVersion: '2019-05-16'
});



app.use(express.static("."));
app.use(express.json());

app.post("/create-setup-intent", async (req, res) => {
  const { items } = req.body;

  // Create a PaymentIntent with the order amount and currency
  const setupIntent = await stripe.setupIntents.create({

  });

  res.send({
    clientSecret: setupIntent.client_secret,
  });
});

app.listen(3000, () => console.log("Node server listening on port 3000!"));