const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();
const cors = require('cors'); 
var http = require('http');
app.engine('html', require('ejs').renderFile);

app.use(express.static("."));
app.use(express.json());
app.set('view engine', 'html');

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/create-checkout-session', cors(), async (req, res) => {
    stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: 'T-shirt',
            },
            unit_amount: 2000,
          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: 'http://localhost:3000',
      cancel_url: 'http://localhost:3000',
    }).then(function (checkout_session) {
      console.log(checkout_session);
      if (checkout_session.error) {
          // Show error to your customer (for example, insufficient funds)
          console.log(checkout_session.error.message);
      } else {
          console.log('Reached the end of Checkout. Redirecting to: ' + checkout_session.url);  
          res.redirect(303, checkout_session.url)
      }
  });
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});
