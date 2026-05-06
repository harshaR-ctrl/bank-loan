document.getElementById('loanForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Hide previous results and errors
    document.getElementById('loanForm').style.display = 'none';
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('resultCard').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';

    // Collect form data
    const formData = {
        age: document.getElementById('age').value,
        income: document.getElementById('income').value,
        loanAmount: document.getElementById('loanAmount').value,
        creditScore: document.getElementById('creditScore').value,
        employmentYears: document.getElementById('employmentYears').value,
        dependents: document.getElementById('dependents').value
    };

    try {
        // Simulate processing delay for better UX
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Send request to backend
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'An error occurred');
        }

        // Hide loading spinner
        document.getElementById('loadingSpinner').style.display = 'none';

        // Display result
        displayResult(data);

    } catch (error) {
        document.getElementById('loadingSpinner').style.display = 'none';
        document.getElementById('loanForm').style.display = 'block';
        document.getElementById('errorMessage').style.display = 'block';
        document.getElementById('errorText').textContent = error.message;
    }
});

function displayResult(data) {
    const resultCard = document.getElementById('resultCard');
    const resultBox = document.getElementById('resultAlert');
    const resultIcon = document.getElementById('resultIcon');
    const resultTitle = document.getElementById('resultTitle');
    const resultProbability = document.getElementById('resultProbability');

    // Reset classes
    resultBox.className = 'result-box';

    // Set result styling based on approval status
    if (data.approved === 1) {
        resultBox.classList.add('success');
        resultIcon.textContent = '✅';
        resultTitle.textContent = data.message;
        resultTitle.style.color = '#059669';
    } else {
        resultBox.classList.add('danger');
        resultIcon.textContent = '❌';
        resultTitle.textContent = data.message;
        resultTitle.style.color = '#dc2626';
    }

    resultProbability.textContent = data.probability + '%';

    // Show result card with animation
    resultCard.style.display = 'block';
}

function resetForm() {
    document.getElementById('loanForm').reset();
    document.getElementById('resultCard').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
    document.getElementById('loanForm').style.display = 'block';
    document.getElementById('age').focus();
}
