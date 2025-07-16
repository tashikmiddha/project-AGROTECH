document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();
  
  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const message = document.getElementById("message");
  const formMessage = document.getElementById("formMessage");

  if (name.value && email.value && message.value) {
    formMessage.style.color = "green";
    formMessage.textContent = "Message sent successfully!";

    // Reset form
    this.reset();
  } else {
    formMessage.style.color = "red";
    formMessage.textContent = "Please fill out all fields.";
  }
});
