function sendMail(contactForm) {
    emailjs.send("service_ld8bf5j", "instacook_template", {
        "user_name": contactForm.user_name.value,
        "user_email": contactForm.user_email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            window.location.replace("thank_you");
        },
        function(error) {
            console.log("FAILED", error);
            window.location.replace("404");
        }
    );
    return false;  // To block from loading a new page
}