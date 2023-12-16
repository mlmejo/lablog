// Function to navigate to the main page
function goToHomepage() {
    // Replace "path/to/main/page" with the actual path to your main page
    window.location.href = "lablog.html";
}

// Function to show the list of students
function goToList() {
    document.getElementById("homepageContent").style.display = "none";
    document.getElementById("studentListSection").style.display = "block";
}

// Function to handle sign-out
function goToSignIn() {
    // Redirect to the sign-in page
    window.location.href = "sign-in.html";
}
// Function to handle sign-out
function signOut() {
    // Redirect to the sign-in page
    window.location.href = "sign-in.html";
}

// Example of how to call the signOut function when the sign-out link is clicked
function goToSignIn() {
    // Call the signOut function
    signOut();
}
