const stripe = require('stripe')('sk_test_51ObRd1ApVXpcEQvtZ3bI4Nh9hqihdFSEmEwaQNK3DXzoX7pTSt2le5Fl7paC96Hw5mDb10e2NZu4aeG5JG69eR2G00vWnfro3T');
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
                currency: 'gbp',
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