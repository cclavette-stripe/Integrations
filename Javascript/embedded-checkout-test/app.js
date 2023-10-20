const stripe = require('stripe')(process.env.SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());



app.get('/', (req, res) => {
    res.sendFile('index.html');
})

app.post('/create-checkout-session', async (req, res) => {
    const session = await stripe.checkout.sessions.create({
        line_items: [{
            price_data: {
                currency: 'eur',
                product_data: {
                    name: 'Something',
                },
                unit_amount: 2000,
            },
            quantity: 1,
        }],
        mode: 'payment',
        ui_mode: 'embedded',
        return_url: 'https://localhost/checkout/return?session_id={CHECKOUT_SESSION_ID}'
    });

    res.send({clientSecret: session.client_secret});
});

app.listen(3000, () => console.log("Server started on :3000"));