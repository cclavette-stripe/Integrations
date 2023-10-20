// This is your test publishable API key.
const stripe = Stripe(
  "pk_test_51Lx7rEBpC6bCE6lLKlxfTqnObWKE1TNQP5S7iC1ImjRZbO7AqvOzpGacVJQEgM6OjcoEpeuSzIqyMJhltyjiW3tD00vH9VGRix",
);

// Initialize Elements which you'll need later
const elements = stripe.elements();

// Use Stripe.js to create a nonce
const cardId = 'ic_1ITi6XKYfU8ZP6raDAXem8ql';
const nonceResult = await stripe.createEphemeralKeyNonce({
  issuingCard: cardId,
});
const nonce = nonceResult.nonce;

// Call your ephemeral key creation endpoint to fetch the ephemeral key
const ephemeralKeyResult = await fetch('/ephemeral-keys', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    card_id: cardId,
    nonce: nonce,
  })
});

const ephemeralKeyResponse = await ephemeralKeyResult.json();
const ephemeralKeySecret = ephemeralKeyResponse.ephemeralKeySecret;