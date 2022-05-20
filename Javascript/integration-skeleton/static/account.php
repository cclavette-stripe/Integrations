
<?php // This is only here to get syntax highlighting. This is an example of an account that can be either verified or not verified.
$account = \Stripe\Account::create([
    'country' => 'CA',
    'type' => 'custom',
    'requested_capabilities' => ['card_payments', 'transfers'],
    'business_type' => 'individual',
    'tos_acceptance' => [
        'date' => time(),
        'ip' => '127.0.0.1'
    ],
    'individual' => [
        'first_name' => 'Test',
        'last_name' => 'Individual',
        'dob' => [
            'day' => 1,
            'month' => 1,
            'year' => 1981
        ],
        'address' => [
            'line1' => '100 E. Harvard Ave.',
            'city' => 'Sainte-Marie',
            'state' => 'QC',
            'postal_code' => 'G6E 9V3'
        ],
        'id_number' => '000000000' // 000000000 for success, 111111111 for identity mismatch
    ],
    'external_account' => [
        'object' => 'bank_account',
        'country' => 'CA',
        'currency' => 'CAD',
        'routing_number' => '11000-000',
        'account_number' => '000123456789',
    ]
]);