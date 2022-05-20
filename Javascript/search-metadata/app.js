const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

const stripe = require('stripe-search-beta')("sk_test_WeTdH0dZDGzU2haZwNWn75LP00kj5GM1Ib")

// You can auto-paginate .search as you can with .list
async function searchFun() {
    const retValue = await stripe.paymentIntents.search({
        query: 'metadata["churn"]:"true"',
        include_count: true,
        //limit: 1,
    }) 

    console.log(retValue);
}

searchFun();
