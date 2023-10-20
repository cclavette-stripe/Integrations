const express = require("express");
const app = express();
const bodyParser = require('body-parser');

// This is your test secret API key.
const stripe = require("stripe")(process.env.ISSUING_SEC_KEY);

app.use(express.static("."));
app.use(express.json());

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/ephemeral-keys', async (request, response) => {
  const { card_id, nonce } = request.body;

  const ephemeralKey = await stripe.ephemeralKeys.create({
    nonce: nonce,
    issuing_card: card_id,
  }, {
    apiVersion: '2022-08-01',
  });

  response.json({
    ephemeralKeySecret: ephemeralKey.secret,
  });
});

app.listen(4242, () => console.log("Node server listening on port 4242!"));