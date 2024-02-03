const express = require('express');
const app = express();

app.use(express.static("."));
app.use(express.json());

// import axios from 'axios';
const axios = require('axios');
const https = require('https'); 
const fs = require('fs');



app.get('/get-confluence-doc', async (req, res) => {
    const httpsAgent = new https.Agent({
        rejectUnauthorized: false,
        cert: fs.readFileSync("./cert.pem"),
        key: fs.readFileSync("./cert.key"),
      })

      axios.defaults.httpsAgent = httpsAgent;

      const request = axios({
        method: 'get',
        url: 'https://confluence.corp.stripe.com/display/DevHelpKB/How+can+you+check+when+a+gate+was+added+or+removed+for+a+merchant',
        headers:{"Authorization": "Bearer NDIyNDI2NjYzNDg0Oq3NvM24KmdXZxOevo1mv333xL99"},
      });

      res.send({
        request: request,
      });
});


app.listen(3000, () => {
    console.log('Running on port 3000');
});
