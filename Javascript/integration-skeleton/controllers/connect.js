const fs = require('fs');
const hex = require('crypto');

// Helper function for converting a CSV to an array
var getCSVArray = function() {
    // Gets the CSV file contents
    var csvFile = fs.readFileSync('static/NamesList.csv', 'utf8', (err, data) => {
        if(err) {
            console.error(err);
            return;
        }
    });

    // Function to split out values into an array using new line as a delimiter
    function csvToArray(str, delimiter = ",") {
        if (on != null) {

        } else {
    
        };

        const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
        const rows = str.slice(str.indexOf("\n") + 1).split("\r\n");
        return rows;
    };
    return csvToArray(csvFile);
};

// Function to get n random names from the list
exports.getRandomName = function(num, on) {
    if (on != undefined) {
        const namesArray = getCSVArray();
        var returnNames = new Object();
    
        for (i = 0; i < num; i++){
            returnNames[i] = namesArray[Math.floor(Math.random() * namesArray.length)]
        };
        return returnNames;
    } else {
        return []
    };
};

// Function to get random email string with 20 character name
exports.getRandomEmail = function(on) {
    if (on != undefined) {
        var first = hex.randomBytes(10).toString('hex');
        var email = first.concat('', '@seedfoundry.com');
        return email;
    } else {
        return null
    };
};

// Function to get random DOB object with data from the 19th century
exports.getRandomDOB = function(on) {
    if (on != undefined) {
        var returnDate = new Object();
    
        var month = Math.floor(Math.random() * 11) + 1;
        var day = Math.floor(Math.random() * 28) + 1;
        var year = Math.floor(Math.random() * 80) + 1920;
    
        returnDate = {
            'month': month,
            'day': day,
            'year': year
        }
        return returnDate;
    } else {
        return null
    };
};

// Function to return object with random address data in the US 
// If the input 'verified' is true, then the address can be validated, otherwise not
exports.getRandomAddress = function(verified, on) {
    var returnAddress = new Object();
    if (on != undefined) {
        if (verified) {
            // Read JSON file and objectify it 
            var JSONFile = fs.readFileSync('static/AddressList.json', 'utf8');
            var addressFile = JSON.parse(JSONFile);
    
            // Get random address from file
            returnAddress = addressFile.addresses[Math.floor(Math.random() * 1000)];
            returnAddress.country = 'US';
            
        } else {
            returnAddress = {
                'address1': '65654 askjndsfla st.', 
                'address2': '',
                'city': 'Eugene',
                'state': 'OR',
                'postalCode': 97402,
                'country': 'US'
            };
        };
        return returnAddress;
    } else {
        returnAddress = {
            'address1': null, 
            'address2': null,
            'city': null,
            'state': null,
            'postalCode': null,
            'country': 'US'
        };
        return returnAddress
    };
};

// Get ID number with 'verified' = true/false
exports.getIDNum = function(verified, on) {
    if (on != undefined){
        if (verified) {
            return '000000000';
        } else {
            return '111111111';
        };
    } else {
        return null
    };
};

// Get random phone number 
exports.getRandomPhone = function(on) {
    if (on != undefined) {
        var phone = Math.floor(Math.random() * 999999) + 1000000;
        return '555'.concat(phone);
    } else {
        return null
    };
};

