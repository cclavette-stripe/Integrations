const stripe = require("stripe")(process.env.SEC_KEY);
const express = require("express");
const app = express();

app.use(express.static("."));
app.use(express.json());

app.post("/webhooks", express.json({ type: "application/json" }), (req, res) => {
  const event = req.body;
  const event_object = event.data.object;
  console.log(event.data);
  // Handle the event
  switch (event.type) {
    case "payment_intent.succeeded":
      console.log(`PaymentIntent for ${event_object.amount} was successful!`);
      break;
    case "payment_intent.canceled":
      console.log(`PaymentIntent for ${event_object.amount} was canceled!`);
      break;
    case "payment_intent.failed":
      console.log(`PaymentIntent for ${event_object.amount} has failed!`);
      break;
    case "payment_intent.processing":
      console.log(
        `PaymentIntent for ${event_object.amount} has started processing!`
      );
      break;
    case "payment_intent.requires_action":
      console.log(`PaymentIntent for ${event_object.amount} requires action!`);
      break;
    case "invoice.created":
      console.log(`Invoice ${event_object.id} created!`);
      console.log(event_object.customer);

      stripe.invoiceItems.create({
        customer: event_object.customer,
        price: "price_1Kv1hjILwdSSnvJbMddwzI2Y",
      });
      break;
    case "invoiceitem.created":
      console.log(`Invoice item ${event_object.id} updated!`);
      break;
    default:
      // Unexpected event type
      console.log(
        `Unhandled event type ${event.type}. Are you sure this event was supposed to go to this endpoint?`
      );
  }

  // Return a 200 response to acknowledge receipt of the event
  res.send();
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
