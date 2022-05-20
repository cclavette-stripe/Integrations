// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe(process.env.PUB_KEY);

// Set up Stripe.js and Elements to use in checkout form
var style = {
    base: {
        color: "#32325d",
    }
};

var createForm = document.getElementById('create-account-form');
var genForm = document.getElementById('generate-link-form');


// Create PI and PM but don't charge PM
createForm.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Gets the value of the button that was pressed and checks to make sure it was the button to create a PI
    let button = document.activeElement.getAttribute('value');

    if (button == 'submit-create') {
        fetch('/create-account', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ test: 'abc123' }),
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                let accountId = data.accountId
                document.querySelector('#account-id').value = accountId
                document.querySelector('#generate-link-form').hidden = false;

                console.log('Standard account created: ' + accountId);
                
            }
        });
    } else {
        return;
    }
});

genForm.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Gets the value of the button that was pressed and checks to make sure it was the button to create a PI
    let button = document.activeElement.getAttribute('value');
    let accountId = document.querySelector('#account-id').value;

    if (button == 'submit-generate') {
        fetch('/generate-link', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ link: accountId }),
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            if (data.error) {
                // Show error to your customer (for example, insufficient funds)
                console.log(data.error.message);
            } else {
                let linkId = data.linkId
                let linkURL = data.linkURL
                console.log('Account link created: ' + linkId);
                console.log('Account link URL here: ' + linkURL);
                document.querySelector('#link-url').value = linkURL
                document.querySelector('#link-url').hidden = false;

            }
        });
    } else {
        return;
    }
});
