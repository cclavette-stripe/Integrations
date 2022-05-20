const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-account', async (req, res) => {
    const account = await stripe.accounts.create({
        type: 'standard',
    });

    res.send({ accountId: account.id });
});

app.post('/generate-link', async (req, res) => {
    let accountId = req.body.link;

    console.log(accountId);

    const accountLink = await stripe.accountLinks.create({
        account: accountId,
        refresh_url: 'http://localhost:3000',
        return_url: 'http://localhost:3000',
        type: 'account_onboarding',
      });

    res.send({ 
        linkId: accountLink.id, 
        linkURL: accountLink.url
    });
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});