const stripe = require("stripe")(process.env.SEC_KEY, {
  betas: ["elements_enable_deferred_intent_beta_1"],
});

document
  .querySelector("#payment-form")
  .addEventListener("submit", handleDiscountCode());

const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  // Fully customizable with appearance API.
  appearance: {
    theme: "night",
    variables: {
      colorPrimary: "#0570de",
      colorBackground: "#ffffff",
      colorText: "#30313d",
      colorDanger: "#df1b41",
      fontFamily: "Ideal Sans, system-ui, sans-serif",
      spacingUnit: "2px",
      borderRadius: "4px",
    },
  },
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

async function handleDiscountCode(code) {
    const { newAmount } = await applyDiscountCode(code);
    elements.update({ amount: newAmount });
  }