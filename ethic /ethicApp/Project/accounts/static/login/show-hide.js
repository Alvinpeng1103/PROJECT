function showHide() {
    // Retrieve elements from html file
    var x = document.getElementById("pass");
    var y = document.getElementById("hide1");
    var z = document.getElementById("hide2");

    // If the type is password -> change to text
    if (x.type === 'password') {
        x.type = "text";
        y.style.display = "block";
        z.style.display = "none";
    } else {
        // If the type is text -> change to password
        x.type = "password";
        y.style.display = "none";
        z.style.display = "block";
    }
}