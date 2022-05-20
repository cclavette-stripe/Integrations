const mock = require('./controllers/connect.js')
const express = require('express');

//express app + layouts
const app = express();
var expressLayouts = require('express-ejs-layouts');
const stripe = require('stripe')(process.env.SEC_KEY);
app.use(express.urlencoded());
app.use(express.static('static'))

// register view engine
app.set('view engine', 'ejs');
app.use(expressLayouts);

// listen for requests (matches top to bottom)
app.listen(3000);

app.get('/', (req, res) => {
    res.render('index');
});

////////////////////////////////////////////////////////////////////////////
///////////////////////////// Connect page /////////////////////////////////
////////////////////////////////////////////////////////////////////////////
app.get('/connect', (req, res) => {
    console.log(req.body);
    console.log(mock.getIDNum(req.body.verified));
    console.log(mock.getRandomAddress(req.body.address));
    res.render('connect');
});

app.post('/create-custom-account', async (req, res) => {
    var name = mock.getRandomName(req.body.name);
    var email = mock.getRandomEmail(req.body.email);
    var dob = mock.getRandomDOB(req.body.dob);
    var addr = mock.getRandomAddress(req.body.address);
    var id_number = mock.getIDNum(req.body.verified, req.body.ssn);
    var phone = mock.getRandomPhone(req.body.phone);

    const account = await stripe.accounts.create({
        country: 'US',
        type: 'custom', 
        capabilities: {
            card_payments: {requested: true},
            transfers: {requested: true},
        },
        business_type: 'individual',
        tos_acceptance: {
            date: Math.round(+new Date()/1000),
            ip: '127.0.0.1'
        },
        individual: {
            email: email,
            first_name: name[0],
            last_name: name[1],
            dob: dob,
            id_number: id_number,
            phone: phone,
            address: {
                city: addr.city,
                country: addr.country,
                line1: addr.address1,
                postal_code: addr.postalCode,
                state: addr.state
            }
        }
    });
    console.log(account.id);
    console.log(account.id_number);
    res.render('index');
});

app.post('/create-account-link', async (req, res) => {
    let id = req.body
    console.log(id);
    const loginLink = await stripe.accounts.createLoginLink(id)
    .then(function (result) {
        return result.json();
    }).then(function(data) {
        res.redirect(data.url);
    });
});

////////////////////////////////////////////////////////////////////////////
///////////////////////////// Payments page ////////////////////////////////
////////////////////////////////////////////////////////////////////////////
app.get('/payments', (req, res) => {
    res.render('payments');
});

app.get('/cancel', (req, res) => {
    res.render('cancel');
});

app.post('/create-checkout-session', async (req, res) => {
    const d = new Date()
    const session = await stripe.checkout.sessions.create({
        line_items: [
        {
            // Provide the exact Price ID (for example, pr_1234) of the product you want to sell
            price: 'price_1KeTy8ILwdSSnvJbhs9C51pb',
            quantity: 1,
        },
        ],
        mode: 'payment',
        expires_at: d.getUTCDate() + 10,
        success_url: `http://localhost:3000`,
        cancel_url: `http://localhost:3000/cancel`,
        automatic_tax: {enabled: true},
    });
    
    res.redirect(303, session.url);
});

////////////////////////////////////////////////////////////////////////////
///////////////////////////// Billing page /////////////////////////////////
////////////////////////////////////////////////////////////////////////////
app.get('/billing', (req, res) => {
    res.render('billing');
});

// 404 page (if no match on any above case)
app.use((req, res) => {
    res.status(404).render('404');
});