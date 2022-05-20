const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-login-link', async (req, res) => {
    const loginLink = await stripe.accounts.createLoginLink(
        'acct_1L0ajSRAzYcRRMwc',
        {
            redirect_url: 'http://127.0.0.1:3000/'
        }
      );

      console.log(loginLink);
      res.redirect(loginLink.url)
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});