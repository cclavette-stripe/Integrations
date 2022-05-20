const stripe = require('stripe')('sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib');
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.get('/', (req, res) => {
    res.send('sendfile');
});

app.post('/create-checkout-session', async (req, res) => {
    const d = Math.round((new Date()).getTime() / 1000 + 3700);

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
        // },
        mode: 'payment',
        expires_at: d,
        automatic_tax: {enabled: true},
        success_url: `http://localhost:3000`,
        cancel_url: `http://localhost:3000/`,
    });
    
    res.redirect(303, session.url);
});

app.post('/expire-checkout-session', async (req, res) => {

    const session = await stripe.checkout.sessions.expire(
        'cs_live_a1K8HBq8bdJ2CMch3Dt11h7KTLRmmz6t8WwdlFj5nVawlLPHhsrRpkouB6'
      );
    
    res.redirect(303, session.url);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});

// 404 page (if no match on any above case)
app.use((req, res) => {
    res.status(404).render('404');
});