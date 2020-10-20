function startAction() {
    var x, text;

    // Get the value of the input field with id="numb"
    x = document.getElementById("numb").value;

    // If x is Not a Number or less than 0 or greater than 10
    if (isNaN(x) || x < 0 || x > 10 || x === "") {
        text = "Input not valid";
        document.getElementById("status").innerHTML = text;
    } else {
        updateUI();
        // send input to API endpoint to start the simulator
        const data = {
            sim_dur_s: x
        }
        fetch('/process', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        setTimeout(updateUI, x * 1000)
    }
}

function updateUI() {

    if (document.getElementById("status").innerHTML === "Simulation running"){
        document.getElementById("status").innerHTML = "Simulation stopped"
    } else {
        document.getElementById("status").innerHTML = "Simulation running"
    }
    
    // changes stop button from being hidden/shown vice versa
    var y = document.getElementById("stopButton");
    if (y.style.display === "none") {
        y.style.display = "block";
    } else {
        y.style.display = "none";
    }

    var z = document.getElementById("startButton");
    if (z.style.display === "none") {
        z.style.display = "block";
    } else {
        z.style.display = "none";
    }
}


function stopAction() {

    // switch the buttons and status
    updateUI();

    // use a duration of -1 to indicate an early term request
    const data = {
        sim_dur_s: "-1"
    }

    fetch('/process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
}