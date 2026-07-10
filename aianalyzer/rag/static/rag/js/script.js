const form = document.querySelector(".chat-form");
const button = document.getElementById("sendBtn");
const textarea = document.querySelector("textarea");

form.addEventListener("submit", () => {

    button.innerHTML = "Thinking...";
    button.disabled = true;

});

textarea.addEventListener("keydown", function(e){

    if(e.key === "Enter" && !e.shiftKey){

        e.preventDefault();

        form.requestSubmit();

    }

});