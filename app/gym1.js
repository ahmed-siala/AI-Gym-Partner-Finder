// Handle form submission for "Create an Account"
document.getElementById('createAccountForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the values entered by the user
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const phone = document.getElementById('phone').value;
    const age = document.getElementById('age').value;

    // Validate if password and confirm password match
    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    // Check if age is valid
    if (age < 18 || age > 40) {
        alert("Please enter a valid age between 18 and 40.");
        return;
    }

    // Optional: You can perform more validations here

    // If everything is valid, redirect to the next page
    window.location.href = 'welcome.html'; // Redirect to another page after successful form submission
});
