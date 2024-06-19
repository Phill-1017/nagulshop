document.addEventListener('DOMContentLoaded', function() {
    const apiBaseURL = 'account';

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
            localStorage.setItem('id', data.id);
            localStorage.setItem('username', data.username);
            localStorage.setItem('role', data.role);

            if (data.role === 'admin') {
                window.location.href = '/home_admin';
            } else if (data.role === 'user') {
                window.location.href = '/home';
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
