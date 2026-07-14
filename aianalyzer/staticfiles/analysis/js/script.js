const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transition = "0.3s";

    });

});

const futureCards = document.querySelectorAll(".future-card");

futureCards.forEach(card => {

    card.addEventListener("click", () => {

        alert("🚀 This feature will be available in a future update!");

    });

});