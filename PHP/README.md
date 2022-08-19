

## Getting Started
First, make sure you have PHP installed. Try the following command.
```
php --version
```
You should see something like this:
```
PHP 8.1.4 (cli) (built: Mar 18 2022 09:45:20) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.4, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.4, Copyright (c), by Zend Technologies
```

If not, install PHP:
```
brew install php
```

After you have cloned the repo, install Composer (PHP Dependency manager) by using the handy `install_composer.sh` script written by `@justinmichael`.  
```
./install_composer.sh
```
You may need to make it executable on your machine(`chmod +x install_composer.sh`).

Once that has run you can install this repo's dependencies like so
```
php composer.phar update
```

Now all your dependencies are in the `vendor` directory and you can import all of them by including `require './vendor/autoload'` at the top of your PHP scripts.

## Create `.env` File
Create a `.env` file alongside the `app.php` and enter the following (swapping your own API key):
```
# Environment variables
STRIPE_SECRET_KEY=sk_test_XXXXXXXX
```

## Test Stripe Integration
Run the following terminal command to verify you have a valid PHP environment set up
```
php app.php
```

You should see your account balance printed as JSON.  If so, you are all set.


## Caveat
This repo uses the current Client/service pattern of PHP as this is what is used across much of Stripe's code snipptes.  You can see a migration guide and some disucssion of legacy patterns in the Stripe PHP library [here](https://github.com/stripe/stripe-php#clientservice-patterns-vs-legacy-patterns).


---
Maintained by [@rmanzer](https://stripe.slack.com/app_redirect?channel=U02HWDC8UER)
