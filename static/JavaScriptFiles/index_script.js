document.addEventListener('DOMContentLoaded', function() {
    const apiBaseURL = 'account'; // Set this to your API's base URL if it's not the same domain

    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch(apiBaseURL + '/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(Object.fromEntries(formData))
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Login failed');
            }
            return response.json();
        })
        .then(data => {
            console.log('Login Success:', data);
            localStorage.setItem('id', data.id);  // Store user ID
            localStorage.setItem('username', data.username);  // Store username
            localStorage.setItem('role', data.role);  // Store role

            // Redirect based on the role
            if (data.role === 'admin') {
                window.location.href = '/home_admin'; // Redirect to admin home page
            } else if (data.role === 'user') {
                window.location.href = '/home'; // Redirect to user home page
            } else {
                alert('Access Denied: You do not have the permissions.');
            }
        })
        .catch(error => {
            console.error('Login Error:', error);
            alert('Login Failed. Check console for more information.');
        });
    });
});
