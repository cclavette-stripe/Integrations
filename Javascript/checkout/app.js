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
        line_items: [
        {
            // Provide the exact Price ID (for example, pr_1234) of the product you want to sell
            price: 'price_1KUgoCILwdSSnvJbHcrS5qHd',
            quantity: 1,
        },
        ],
        // automatic_tax: {
        //     enabled: 'true',
        // },d
        mode: 'payment',
        automatic_tax: {enabled: true},
        success_url: `http://localhost:3000`,
        cancel_url: `http://localhost:3000/`,
    });
    
    res.redirect(303, session.url);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});
