const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());
app.engine('html', require('ejs').renderFile);


app.get('/', (req, res) => {
    res.send('sendfile');
});

app.post('/create-checkout-session', async (req, res) => {
    const session = await stripe.checkout.sessions.create({
        mode: 'subscription',
        line_items: [
            {
                price: 'price_1MS5VYILwdSSnvJbwtONsNn4',
                quantity: 1,
            },
        ],
        allow_promotion_codes: true,
        success_url: `https://www.example.com`,
        cancel_url: 'https://www.example.com',
    
        automatic_tax: {
            enabled: true,
        },
        billing_address_collection: 'required',
    });
    
    res.redirect(303, session.url);
});

app.listen(4242, () => {
    console.log('Running on port 4242');
});
