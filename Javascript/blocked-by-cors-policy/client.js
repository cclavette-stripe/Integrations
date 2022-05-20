// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe("pk_test_RDRfnGAPN0nn2zXL7zkWFrEz");

var form = document.getElementById("create-checkout-session");

// Handles the refund button
form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  fetch("/create-checkout-session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    }).then(function (result) {
        return result.json();
    }).then(function (data) {
        if (data.error) {
            // Show error to your customer (for example, insufficient funds)
            console.log(data.error.message);
        } else {
            console.log("Payment has been refunded!");
        }
    });
});
