<?php
require './vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


$key = $_ENV['STRIPE_SECRET_KEY'];
$stripe = new Stripe\StripeClient($key);
$cs = $stripe->checkout->sessions->retrieve(
    'cs_test_b1jwwY66w1bJgeyWNfig5vyau855f3iKUOMP8fOaWUHfYe6G3ovhzyGsVo'
  );

$customer = $stripe->customers->retrieve($cs->customer);

// echo $cs;
echo $customer->id;