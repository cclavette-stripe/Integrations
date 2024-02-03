
var form = document.getElementById('get-doc');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Gets the value of the button that was pressed
    let button = document.activeElement.getAttribute('value');

    if (button == 'submit-get') {
        fetch('/get-confluence-doc', {
            method: "GET",
        }).then(function (result) {
            return result.json();
        }).then(function (data) {
            
        });
    } else {
        return('No button name');
    }
});
