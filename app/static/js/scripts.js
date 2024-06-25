
// New form validation code
document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (e) => {
        const username = document.querySelector('#username').value;
        const email = document.querySelector('#email').value;
        const password = document.querySelector('#password').value;
        const password2 = document.querySelector('#password2').value;

        if (username === '' || email === '' || password === '' || password2 === '') {
            alert('All fields are required!');
            e.preventDefault(); // Prevent form submission
        } else if (password !== password2) {
            alert('Passwords do not match!');
            e.preventDefault(); // Prevent form submission
        }
    });
});