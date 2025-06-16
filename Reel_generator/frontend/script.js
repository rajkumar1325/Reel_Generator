function generateReel() {
    const prompt = document.getElementById('promptInput').value;
    const statusElem = document.getElementById('status');
    const scriptElem = document.getElementById('scriptOutput');

    // if only blank spaces are +nt.
    if (!prompt.trim()) {
        alert('Please enter a topic!');
        return;
    }

    statusElem.innerText = 'Generating Reel Script... Please wait.';
    scriptElem.innerText = '';  // Clear previous script

    fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        if(data.status === 'success') {
            statusElem.innerText = 'Reel Script Generated Successfully!';
            scriptElem.innerText = data.script;  // Show script here
        } else {
            statusElem.innerText = 'Error: ' + data.message;
        }
    })
    .catch(error => {
        statusElem.innerText = 'Error generating reel.';
        console.error('Error:', error);
    });
}
