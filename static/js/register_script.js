function toggleAdminPassword() {
    const roleSelect = document.getElementById('role');
    const adminPassContainer = document.getElementById('adminPassContainer');
    adminPassContainer.style.display = roleSelect.value === 'admin' ? 'block' : 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    const apiBaseURL = 'account';

    document.getElementById('registerForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const role = document.getElementById('role').value;
        const adminPassword = document.getElementById('adminPassword').value;
        const formData = new FormData(this);

        if (role === 'admin' && adminPassword !== 'ADMIN') {
            alert('Incorrect admin password.');
            return;
        }

        fetch(apiBaseURL + '/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(Object.fromEntries(formData))
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Registration failed');
            }
            return response.json();
        })
        .then(data => {
            console.log('Registration Success:', data);
            alert('Registration Successful!');
            window.location.href = '/';
        })
        .catch(error => {
            console.error('Registration Error:', error);
            alert('Registration Failed. Check console for more information.');
        });
    });
});
