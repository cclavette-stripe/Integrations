const stripe = require("stripe")(process.env.SEC_KEY, {
  apiVersion: "2023-10-16",
});
const express = require("express");
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post("/create-payment-intent", async (req, res) => {
  const prices = await stripe.prices.list();
  console.log(prices);
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
