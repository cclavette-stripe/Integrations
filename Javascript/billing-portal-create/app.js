const stripe = require('stripe')('sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib');
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-portal-session', async (req, res) => {
    // Authenticate your user.
    const session = await stripe.billingPortal.sessions.create({
      customer: 'cus_Ld5HFiFN9EzsXW',
      return_url: 'http://localhost:3000',
    });
  
    res.redirect(session.url);
  });

app.listen(3000, () => {
    console.log('Running on port 3000');
});
