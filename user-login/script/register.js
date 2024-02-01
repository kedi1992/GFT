function registerUser() {
    // Get form data
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        dateOfBirth: document.getElementById('dateOfBirth').value,
        phoneNumber: document.getElementById('phoneNumber').value,
    };

    // Make API request using Axios
    axios.post('http://127.0.0.1:8000/user/api/register/', formData)
        .then(response => {
            // Handle successful registration
            console.log('User registered successfully:', response.data);
            alert('User registered successfully!');
        })
        .catch(error => {
            // Handle registration error
            console.error('Registration error:', error.response.data);
            alert('Registration error. Please check the form and try again.');
        });
}
