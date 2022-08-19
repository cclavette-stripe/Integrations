<?php
require './vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


$key = $_ENV['STRIPE_SECRET_KEY'];
$stripe = new Stripe\StripeClient($key);
$balance = $stripe->balance->retrieve();


echo $balance;
