const stripe = require('stripe')('sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib');
const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

const get_config = async () => {
  // Authenticate your user.
  const configuration = await stripe.billingPortal.configurations.create({
    features: {
      customer_update: {
        allowed_updates: ['email', 'tax_id'],
        enabled: true,
      },
    },
    business_profile: {
      privacy_policy_url: 'https://example.com/privacy',
      terms_of_service_url: 'https://example.com/terms',
    },
  });

  return configuration;
};

app.post('/create-portal-session', async (req, res) => {
  const config = await get_config();  
  
  // Authenticate your user.
  const session = await stripe.billingPortal.sessions.create({
    configuration: config.id,
    customer: 'cus_Ld5HFiFN9EzsXW',
    return_url: 'http://localhost:3000',
  });
  
  res.redirect(session.url);
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});
