const stripe = require('stripe')(process.env.IN_SEC_KEY);
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post('/create-payment-intent', async (req, res) => {
    const paymentIntent = await stripe.paymentIntents.create({
        amount: 1099,
        currency: 'inr',
        capture_method: 'manual',
        automatic_payment_methods: {
            enabled: true,
        },
    });

    res.send({ clientSecret: paymentIntent.client_secret });
});

app.post('/cancel-payment-intent', async (req, res) => {
    let paymentIntentId = req.body.pi;
    console.log('Cancelling payment intent: ' + paymentIntentId);

    const cancelledIntent = await stripe.paymentIntents.cancel(
        paymentIntentId
      );

    res.send({ cancelledIntent: cancelledIntent.id });
});

// Creates customer AND attaches the payment method AND attaches the customer to the PI
app.post('/create-customer', async (req, res) => {
    let paymentMethodId = req.body.pm;
    let paymentIntentId = req.body.pi;
    console.log('Creating customer with payment method: ' + paymentMethodId);

    const customer = await stripe.customers.create({
        payment_method: paymentMethodId
    });

    console.log('Customer created: ' + customer.id);

    const paymentIntent = await stripe.paymentIntents.update(
        paymentIntentId,
        {
            customer: customer.id,
            setup_future_usage: 'off_session',
        }
      );

    console.log('Payment intent updated: ' + paymentIntent.id);

    res.send({ paymentIntent: paymentIntent });
});

app.post('/refund-payment-intent', async (req, res) => {
    let paymentIntentId = req.body.pi;
    console.log('Refunding payment intent: ' + paymentIntentId);

    const refundedIntent = await stripe.refunds.create({
        payment_intent: paymentIntentId
    });

    res.send({ refundedIntent: refundedIntent.id });
});

app.post('/full-payment-intent', async (req, res) => {
    let paymentIntentId = req.body.pi;
    console.log('Capturing payment intent: ' + paymentIntentId);

    const capturedIntent = await stripe.paymentIntents.capture(
        paymentIntentId
      );

    res.send({ capturedIntent: capturedIntent.id });
});

app.post('/partial-payment-intent', async (req, res) => {
    let paymentIntentId = req.body.pi;
    let amount = req.body.a;

    console.log('Capturing payment intent: ' + paymentIntentId);

    const capturedIntent = await stripe.paymentIntents.capture(paymentIntentId, {
            amount_to_capture: amount,
        }
      );

    res.send({ capturedIntent: capturedIntent.id });
});
 
app.post('/payment-intent-webhooks', express.json({ type: 'application/json' }), (req, res) => {
    const event = req.body;
    const paymentIntent = event.data.object;
    // Handle the event
    switch (event.type) {
        case 'payment_intent.succeeded':
            console.log(`PaymentIntent for ${paymentIntent.amount} was successful!`);
            break;
        case 'payment_intent.canceled':
            console.log(`PaymentIntent for ${paymentIntent.amount} was canceled!`);
            break;
        case 'payment_intent.failed':
            console.log(`PaymentIntent for ${paymentIntent.amount} has failed!`);
            break;
        case 'payment_intent.processing':
            console.log(`PaymentIntent for ${paymentIntent.amount} has started processing!`);
            break;
        case 'payment_intent.requires_action':
            console.log(`PaymentIntent for ${paymentIntent.amount} requires action!`);
            break;
        default:
            // Unexpected event type
            console.log(`Unhandled event type ${event.type}. Are you sure this event was supposed to go to this endpoint?`);
    }

    // Return a 200 response to acknowledge receipt of the event
    res.send();
});


app.listen(3000, () => {
    console.log('Running on port 3000');
});