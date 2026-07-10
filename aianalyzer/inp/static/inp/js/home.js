const form = document.querySelector("form");

form.addEventListener("submit", () => {

    const button = document.querySelector(".btn");

    button.innerHTML = "Analyzing...";

    button.disabled = true;

});