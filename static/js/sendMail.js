
const messageContainer = document.getElementById('message')
function sendMail(contactForm) {
    emailjs.send("service_xhz66xf", "fussypussy_template", {
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.emailaddress.value,
        "message_content": contactForm.messagecontent.value
    })
    .then(
        function(response) {
            messageContainer.classList.add('success')
            messageContainer.textContent = 'Thanks for your message! We\'ll be in touch soon!';
            return("SUCCESS", response);
        },
        function(error) {
            messageContainer.classList.add('error')
            messageContainer.textContent = 'Oops! There was an error in seind your message! Try again!';
            return("FAILED", error);
        }
    );
    // return false;
}