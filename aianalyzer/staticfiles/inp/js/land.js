// ===============================
// MOBILE NAVIGATION
// ===============================

const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

if (menuBtn && navLinks) {

    menuBtn.addEventListener("click", () => {

        navLinks.classList.toggle("active");

        const icon = menuBtn.querySelector("i");

        if (navLinks.classList.contains("active")) {
            icon.classList.remove("fa-bars");
            icon.classList.add("fa-times");
        } else {
            icon.classList.remove("fa-times");
            icon.classList.add("fa-bars");
        }

    });

}

// ===============================
// CLOSE MOBILE MENU AFTER CLICK
// ===============================

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

        const icon = menuBtn.querySelector("i");

        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");

    });

});

// ===============================
// NAVBAR SCROLL EFFECT
// ===============================

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        navbar.style.background = "rgba(5,8,22,0.96)";
        navbar.style.boxShadow = "0 8px 30px rgba(0,0,0,.35)";

    } else {

        navbar.style.background = "rgba(5,8,22,.75)";
        navbar.style.boxShadow = "none";

    }

});

// ===============================
// SMOOTH SCROLL
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(
            this.getAttribute("href")
        );

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

// ===============================
// ACTIVE NAVIGATION
// ===============================

const sections = document.querySelectorAll("section");
const navItems = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 150;

        if (window.scrollY >= sectionTop) {

            current = section.getAttribute("id");

        }

    });

    navItems.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {

            link.classList.add("active");

        }

    });

});

// ===============================
// SCROLL REVEAL
// ===============================

const revealElements = document.querySelectorAll(
    ".feature-card, .step, .tech-box, .cta"
);

const reveal = () => {

    revealElements.forEach(el => {

        const top = el.getBoundingClientRect().top;

        const visible = 150;

        if (top < window.innerHeight - visible) {

            el.style.opacity = "1";
            el.style.transform = "translateY(0)";

        }

    });

};

reveal();

window.addEventListener("scroll", reveal);

// ===============================
// INITIAL STATE FOR REVEAL
// ===============================

revealElements.forEach(el => {

    el.style.opacity = "0";
    el.style.transform = "translateY(50px)";
    el.style.transition = "all .8s ease";

});

// ===============================
// HERO FLOAT EFFECT
// ===============================

const heroCard = document.querySelector(".hero-card");

document.addEventListener("mousemove", (e) => {

    if (!heroCard) return;

    const x = (window.innerWidth / 2 - e.pageX) / 45;

    const y = (window.innerHeight / 2 - e.pageY) / 45;

    heroCard.style.transform =
        `rotateY(${x}deg) rotateX(${-y}deg)`;

});

document.addEventListener("mouseleave", () => {

    if (!heroCard) return;

    heroCard.style.transform = "rotateX(0) rotateY(0)";

});

// ===============================
// BUTTON RIPPLE EFFECT
// ===============================

const buttons = document.querySelectorAll(
    ".primary-btn, .secondary-btn, .cta-btn"
);

buttons.forEach(button => {

    button.addEventListener("click", function (e) {

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
    "%c🚀 AI Video Analyzer Loaded Successfully",
    "color:#06B6D4;font-size:16px;font-weight:bold;"
);