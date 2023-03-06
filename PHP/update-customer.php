<?php
require './vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


$key = $_ENV['STRIPE_SECRET_KEY'];
$stripe = new Stripe\StripeClient($key);

$paymentIntent =  $stripe->paymentIntents->retrieve(
  'pi_1HruFYILwdSSnvJbjey4lywv',
  []
);


echo $paymentIntent->id;
