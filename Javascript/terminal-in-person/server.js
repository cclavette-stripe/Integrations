const express = require("express");
const app = express();
// This is your test secret API key.
const stripe = require("stripe")("sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib");

app.use(express.static('views'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// For EJS
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

// For styling
app.use(express.static(__dirname + '/public'));

app.get("/", async(req, res) => {
  res.render('index')
});

// The ConnectionToken's secret lets you connect to any Stripe Terminal reader
// and take payments with your Stripe account.
// Be sure to authenticate the endpoint for creating connection tokens.
app.post("/connection_token", async(req, res) => {
  let connectionToken = await stripe.terminal.connectionTokens.create();
  res.json({secret: connectionToken.secret});
})

app.post("/create_payment_intent", async(req, res) => {
  // For Terminal payments, the 'payment_method_types' parameter must include
  // 'card_present' and the 'capture_method' must be set to 'manual'
  const intent = await stripe.paymentIntents.create({
    amount: req.body.amount,
    currency: 'usd',
    payment_method_types: [
      'card_present',
    ],
    capture_method: 'manual',
  });
  res.json({client_secret: intent.client_secret});
})

app.post("/capture_payment_intent", async(req, res) => {
  const intent = await stripe.paymentIntents.capture(req.body.id);
  res.send(intent);
})

app.listen(4242, () => console.log('Node server listening on port 4242!'));
