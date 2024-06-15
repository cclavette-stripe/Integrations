<?php
require './vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


$key = $_ENV['STRIPE_SECRET_KEY'];
$stripe = new Stripe\StripeClient($key);

$paymentIntent = $stripe->paymentIntents->create(
  [
      'amount' => 1111,
      'currency' => 'usd',
      'payment_method_types' => ['card_present'],
      'capture_method' => 'automatic_async',
      'transfer_data' => [
          'amount' =>  111,
          'destination' => 'acct_1OXuC0RDN4wWBeiY',
      ],
      //get package and determine percent to charge for fee.
      //'tax' => $totaltax,
      //'application_fee_amount' => 5,
      //'processing' => 5
  ]
);


echo $paymentIntent->id;
