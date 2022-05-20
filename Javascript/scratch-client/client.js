// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe(process.env.PUB_KEY);

// Set up Stripe.js and Elements to use in checkout form
var style = {
    base: {
        color: "#32325d",
    }
};

var form = document.getElementById('payment-form');

// Create PI and PM but don't charge PM
form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Gets the value of the button that was pressed and checks to make sure it was the button to create a PI
    let button = document.activeElement.getAttribute('value');

    if (button == 'submit-create') {
        fetch('/create-payment-intent', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ test: 'abc123' }),
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            
        });
    } else {
        return;
    }
});
