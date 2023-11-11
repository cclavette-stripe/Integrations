// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys

var stripe = Stripe(
  "pk_test_51E7YoAILwdSSnvJbYXbLCN7UWIIdQqSL7pylRkdnvviU67fEUa4NOS0FnHThGINQNpgt2mEFvs3DgZCG5r78XrDZ00FzYvokfs"
);
var elements = stripe.elements();
var form = document.getElementById("payment-form");

// Set up Stripe.js and Elements to use in checkout form
var style = {
  base: {
    color: "#32325d",
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', ({error}) => {
  let displayError = document.getElementById('card-errors');
  if (error) {
    displayError.textContent = error.message;
  } else {
    displayError.textContent = '';
  }
});


form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  // Gets the value of the button that was pressed and checks to make sure it was the button to create a PI
  let button = document.activeElement.getAttribute("value");

  if (button == "card-element") {
    fetch("/create-payment-intent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ test: "abc123" }),
    })
      .then(function (result) {
        return result.json();
      }).then(
        stripe.confirmCardPayment({
          payment_method: {
            card: card,
            billing_details: {
              name: 'Jenny Rosen'
            }
          },
          setup_future_usage: 'off_session'
        }).then(function(result) {
          if (result.error) {
            // Show error to your customer
            console.log(result.error.message);
          } else {
            if (result.paymentIntent.status === 'succeeded') {
              // Show a success message to your customer
              // There's a risk of the customer closing the window before callback execution
              // Set up a webhook or plugin to listen for the payment_intent.succeeded event
              // to save the card to a Customer
        
              // The PaymentMethod ID can be found on result.paymentIntent.payment_method
            }
          }
        })
      )}
    });
    