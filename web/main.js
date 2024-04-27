document.getElementById('articleForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const articleText = document.getElementById('articleText').value;

    // This should work directly for the most of you if not just Replace 'http://0.0.0.0:8000/categorize' with the correct API endpoint
    fetch('http://localhost:8000/categorize', { 

        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: articleText })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data); 
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (results.category) {
        resultsDiv.innerHTML = `<p><strong>Category:</strong> ${results.category}</p>`;
    } else {
        resultsDiv.innerHTML = '<p>Error: Unable to classify article.</p>';
    }
}
