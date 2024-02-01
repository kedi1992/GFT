

// Function to perform login
const performLogin = async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        // Make a POST request to the Django REST Framework login API
        const response = await axios.post('http://127.0.0.1:8000/user/api/token/', {
            username: username,
            password: password,
        });

        // Access the token from the response data
        const token = response.data.access;

        // Save the token to local storage or a secure storage mechanism
        localStorage.setItem('token', token);

        // Perform any other necessary actions (e.g., redirect to another page)
        window.location.href = '/dashboard'; // Replace with your desired redirection path
    } catch (error) {
        // Handle login error
        const errorMessage = error.response.data.non_field_errors[0] || 'Login failed. Please try again.';
        document.getElementById('login-error').innerText = errorMessage;
    }
};
