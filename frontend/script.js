document
  .getElementById("userForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch("/submit", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((message) => {
        document.getElementById("message").textContent = message;
      })
      .catch((error) => console.error("Error:", error));
  });
