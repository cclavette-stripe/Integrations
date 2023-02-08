const stripe = Stripe(
  "pk_test_51E7YoAILwdSSnvJbYXbLCN7UWIIdQqSL7pylRkdnvviU67fEUa4NOS0FnHThGINQNpgt2mEFvs3DgZCG5r78XrDZ00FzYvokfs",
  {
    betas: ["elements_enable_deferred_intent_beta_1"],
  }
);

const appearance = {
  theme: "night",
  variables: {
    colorPrimary: "#0570de",
  },
};

const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  // Fully customizable with appearance API.
  appearance: appearance,
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options, appearance);

// Create and mount the Payment Element
const paymentElement = elements.create("payment", {
  layout: {
    type: "tabs",
    defaultCollapsed: false,
  },
});
paymentElement.mount("#payment-element");

const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Create the PaymentIntent
  const response = await fetch("/create-intent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  }).then(function (result) {
    return result.json();
  });

  const clientSecret = response.client_secret;

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
