// Script untuk halaman index.html
// Mengirim data form ke server saat tombol "Predict Now" ditekan
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    const jsonData = {};
    for (const [key, value] of formData.entries()) {
        jsonData[key] = value;
    }
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        const resultText = document.getElementById('result-text');
        if (data.prediction) {
            resultText.textContent = `Mobile price range should be ${data.prediction}`;
        } else {
            resultText.textContent = 'Prediction failed. Please try again.';
        }
        window.location.href = '/result';
    })
    .catch(error => {
        console.error('Error:', error);
        const resultText = document.getElementById('result-text');
        resultText.textContent = 'Prediction failed. Please try again.';
        window.location.href = '/result';
    });
});

// Script untuk halaman result.html
// Mengecek apakah ada hasil prediksi yang diterima dari server
document.addEventListener('DOMContentLoaded', function() {
    const resultText = document.getElementById('result-text');
    if (!resultText.textContent) {
        window.location.href = '/';
    }
});
