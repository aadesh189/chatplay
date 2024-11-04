function respload() {
    // Update UI to indicate loading state
    document.getElementById('airesp1').value = 'Generating AI Response...';
    document.getElementById('token_id').value = '...';
    document.getElementById('total_cost').value = '...';

    // Retrieve input values
    const systemPrompt = document.getElementById('sysprmpt').value;
    const userPrompt = document.getElementById('useprmpt').value;
    const selectedModel = document.getElementById('model').value;

    // Log inputs for debugging
    console.log('System Prompt:', systemPrompt);
    console.log('User Prompt:', userPrompt);
    console.log('Selected Model:', selectedModel);

    // Prepare data for the request
    const requestData = {
        system: systemPrompt,
        user: userPrompt,
        choicemodel: selectedModel
    };

    // Fetch API request
    fetch('http://localhost:5000/prmpt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Update UI with received data
        document.getElementById('airesp1').value = data.sysdata;
        document.getElementById('token_id').value = data.token;
        document.getElementById('total_cost').value = data.cost;
    })
    .catch(error => {
        console.error('Error: ', error);
        alert('An error occurred while generating the response. Please try again.');
    });
}
