// ===============================
// PASSWORD TOGGLE
// ===============================

document.querySelectorAll(".toggle-password").forEach(toggle => {

    toggle.addEventListener("click", () => {

        const input = toggle.previousElementSibling;

        if (input.type === "password") {

            input.type = "text";

            toggle.classList.remove("fa-eye");
            toggle.classList.add("fa-eye-slash");

        } else {

            input.type = "password";

            toggle.classList.remove("fa-eye-slash");
            toggle.classList.add("fa-eye");

        }

    });

});

// ===============================
// PASSWORD STRENGTH
// ===============================

const password = document.querySelector("#id_password1");

const strength = document.querySelector(".password-strength");

if (password && strength) {

    password.addEventListener("input", () => {

        const value = password.value;

        let score = 0;

        if (value.length >= 8) score++;

        if (/[A-Z]/.test(value)) score++;

        if (/[a-z]/.test(value)) score++;

        if (/[0-9]/.test(value)) score++;

        if (/[^A-Za-z0-9]/.test(value)) score++;

        if (score <= 2) {

            strength.textContent = "Weak";
            strength.style.color = "#EF4444";

        }

        else if (score <= 4) {

            strength.textContent = "Medium";
            strength.style.color = "#F59E0B";

        }

        else {

            strength.textContent = "Strong";
            strength.style.color = "#10B981";

        }

    });

}

// ===============================
// CONFIRM PASSWORD CHECK
// ===============================

const password1 = document.querySelector("#id_password1");

const password2 = document.querySelector("#id_password2");

const match = document.querySelector(".password-match");

if (password1 && password2 && match) {

    password2.addEventListener("input", () => {

        if (password2.value.length === 0) {

            match.textContent = "";

            return;

        }

        if (password1.value === password2.value) {

            match.textContent = "Passwords match";

            match.style.color = "#10B981";

        }

        else {

            match.textContent = "Passwords do not match";

            match.style.color = "#EF4444";

        }

    });

}

// ===============================
// INPUT ANIMATION
// ===============================

document.querySelectorAll("input").forEach(input => {

    input.addEventListener("focus", () => {

        input.parentElement.classList.add("focused");

    });

    input.addEventListener("blur", () => {

        if (input.value === "") {

            input.parentElement.classList.remove("focused");

        }

    });

});

// ===============================
// BUTTON LOADING
// ===============================

const form = document.querySelector("form");

const button = document.querySelector(".auth-btn");

if (form && button) {

    form.addEventListener("submit", () => {

        button.disabled = true;

        button.innerHTML =
            '<i class="fas fa-spinner fa-spin"></i> Please wait...';

    });

}

// ===============================
// FADE IN
// ===============================

window.addEventListener("load", () => {

    const card = document.querySelector(".auth-card");

    if (!card) return;

    card.style.opacity = "0";

    card.style.transform = "translateY(30px)";

    setTimeout(() => {

        card.style.transition = "all .7s ease";

        card.style.opacity = "1";

        card.style.transform = "translateY(0)";

    }, 100);

});

// ===============================
// FLOATING CARD EFFECT
// ===============================

const card = document.querySelector(".auth-card");

document.addEventListener("mousemove", (e) => {

    if (!card) return;

    const x = (window.innerWidth / 2 - e.pageX) / 60;

    const y = (window.innerHeight / 2 - e.pageY) / 60;

    card.style.transform =
        `rotateY(${x}deg) rotateX(${-y}deg)`;

});

document.addEventListener("mouseleave", () => {

    if (!card) return;

    card.style.transform = "rotateX(0deg) rotateY(0deg)";

});

// ===============================
// BUTTON RIPPLE
// ===============================

document.querySelectorAll(".auth-btn").forEach(btn => {

    btn.addEventListener("click", function(e) {

        const ripple = document.createElement("span");

        const rect = this.getBoundingClientRect();

        const size = Math.max(rect.width, rect.height);

        ripple.style.width = ripple.style.height = size + "px";

        ripple.style.left =
            e.clientX - rect.left - size / 2 + "px";

        ripple.style.top =
            e.clientY - rect.top - size / 2 + "px";

        ripple.className = "ripple";

        this.appendChild(ripple);

        setTimeout(() => {

            ripple.remove();

        }, 600);

    });

});

// ===============================
// CONSOLE MESSAGE
// ===============================

console.log(
    "%c🔐 Authentication Ready",
    "color:#06B6D4;font-size:15px;font-weight:bold;"
);