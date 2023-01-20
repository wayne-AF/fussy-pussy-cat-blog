function sendMail(contactForm) {
    emailjs.send("service_xhz66xf", "fussypussy_template", {
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.emailaddress.value,
        "message_content": contactForm.messagecontent.value
    })
    .then(
        function(response) {
            return("SUCCESS", response);
        },
        function(error) {
            return("FAILED", error);
        }
    );
    // return false;
}