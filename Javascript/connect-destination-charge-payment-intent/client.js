var stripe = Stripe(process.env.PUB_KEY);
var elements = stripe.elements();

// Set up Stripe.js and Elements to use in checkout form
var style = {
    base: {
        color: "#32325d",
    }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', ({ error }) => {
    let displayError = document.getElementById('card-errors');
    if (error) {
        displayError.textContent = error.message;
    } else {
        displayError.textContent = '';
    }
});

var form = document.getElementById('payment-form');
var confirmForm = document.getElementById('confirm-form');
var captureForm = document.getElementById('capture-form');
var refundForm = document.getElementById('refund-form');

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
            let clientSecret = data.clientSecret
            document.querySelector('#client-secret').value = clientSecret

            // Stripe JS method
            stripe.createPaymentMethod({
                type: 'card',
                card: card,
                billing_details: {
                    name: 'Flem Wendle',
                },
            }).then(function (data) {
                // Check for errors when creating the payment method
                if (data.error) {
                    // Show error to your customer (for example, insufficient funds)
                    console.log(data.error.message);
                } else {
                    console.log('Payment method created!');
                    let paymentMethod = data.paymentMethod;
                    
                    document.querySelector('#payment-method').value = paymentMethod.id;
                    document.querySelector('#confirm-form').hidden = false;
                }
            });
        });
    } else {
        return;
    }
});

// Event listener for the confirm, cancel and save buttons
confirmForm.addEventListener('submit', function (ev) {
    ev.preventDefault();
    let button = document.activeElement.getAttribute('value');
    let clientSecret = document.querySelector('#client-secret').value;
    let paymentMethod = document.querySelector('#payment-method').value;

    // Checks to make sure the button pressed was either "submit-confirm" or "submit-cancel" before confirming the PI
    if (button == 'submit-confirm') {
        // Stripe JS method
        stripe.confirmCardPayment(clientSecret, {
            payment_method: paymentMethod,  
        }).then(function(data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                let paymentIntentId = data.paymentIntent.id
                console.log('Payment intent confirmed!');
                document.querySelector('#capture-form').hidden = false;
                document.querySelector('#payment-intent').value = paymentIntentId;
                document.querySelector('#hidden-save').hidden = true;
            };
        });
    } else if (button == 'submit-cancel') {
        
        stripe.retrievePaymentIntent(clientSecret)
        .then(function(data) {
            let paymentIntentId = data.paymentIntent.id;
            fetch('/cancel-payment-intent', {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ pi: paymentIntentId }), 
            }).then(function (result) {
                return result.json();
            }).then(function (data) {
                if (data.error) {
                    // Show error to your customer (for example, insufficient funds)
                    console.log(data.error.message);
                } else {
                    document.querySelector('#hidden-cancel').hidden = false;
                    document.querySelector('#refund-payment').value = paymentIntentId;
                    document.querySelector('#cancel-form').hidden = false;
                    document.querySelector('#hidden-save').hidden = true;
                };
            });
        });
    } else if (button == 'submit-save') {
        
        stripe.retrievePaymentIntent(clientSecret)
        .then(function(data) {
            let paymentIntentId = data.paymentIntent.id;
            fetch('/create-customer', {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ 
                    pm: paymentMethod,
                    pi: paymentIntentId
                }), 
            }).then(function (result) {
                return result.json();
            }).then(function (data) {
                if (data.error) {
                    // Show error to your customer (for example, insufficient funds)
                    console.log(data.error.message);
                } else {
                    document.querySelector('#hidden-save').hidden = false;
                };
            });
        });
    } else {
        return;
    }
});

// Event listener for when the PI is captured
captureForm.addEventListener('submit', function (ev) {
    ev.preventDefault();

    let button = document.activeElement.getAttribute('value');
    let paymentIntentId = document.querySelector('#payment-intent').value

    if (button == 'submit-full') {
        fetch('/full-payment-intent', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pi: paymentIntentId }), 
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                document.querySelector('#hidden-full').hidden = false;
                document.querySelector('#refund-form').hidden = false;
                document.querySelector('#capture-form').hidden = true;
                document.querySelector('#refund-payment').value = paymentIntentId;
                document.querySelector('#payment-intent').value = paymentIntentId;
            };
        });
    } else if (button == 'submit-partial') {
        let amount = document.querySelector('#charge-amount').value

        fetch('/partial-payment-intent', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                pi: paymentIntentId,
                a: amount,
                }), 
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                document.querySelector('#hidden-partial').hidden = false;
                document.querySelector('#refund-form').hidden = false;
                document.querySelector('#capture-form').hidden = true;
                document.querySelector('#refund-payment').value = paymentIntentId;
                document.querySelector('#payment-intent').value = paymentIntentId;
            };
        });
    } else {
        return;
    }
});
 
// Handles the refund button
refundForm.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Gets the value of whatever elements is active (e.g. button that was pressed) and checks to make sure it was the button to create a PI
    let button = document.activeElement.getAttribute('value');
    let paymentIntentId = document.querySelector('#refund-payment').value;

    if (button == 'submit-refund') {
        fetch('/refund-payment-intent', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pi: paymentIntentId }),
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                console.log('Payment has been refunded!');
                
                document.querySelector('#hidden-refund').hidden = false;
            }
        });
    } else {
        return;
    }
});