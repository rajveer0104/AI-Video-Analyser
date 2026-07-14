// ===============================================
// AI Video Analyzer
// script.js
// ===============================================

document.addEventListener("DOMContentLoaded", () => {

    // ==========================================
    // DOM Elements
    // ==========================================

    const form = document.getElementById("chatForm");
    const textarea = document.getElementById("questionInput");

    const loadingOverlay = document.getElementById("loadingOverlay");

    const copyBtn = document.getElementById("copyAnswer");
    const answerText = document.getElementById("answerText");

    const suggestionButtons =
        document.querySelectorAll(".suggestion-btn");



    // ==========================================
    // Autofocus
    // ==========================================

    if (textarea) {
        textarea.focus();
    }



    // ==========================================
    // Suggested Questions
    // ==========================================

    suggestionButtons.forEach(button => {

        button.addEventListener("click", () => {

            textarea.value = button.innerText;

            textarea.focus();

            textarea.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        });

    });



    // ==========================================
    // Submit Form
    // ==========================================

    if (form) {

        form.addEventListener("submit", () => {

            if (loadingOverlay) {

                loadingOverlay.style.display = "flex";

            }

        });

    }



    // ==========================================
    // Enter to Send
    // Shift + Enter -> New Line
    // ==========================================

    if (textarea && form) {

        textarea.addEventListener("keydown", function (e) {

            if (e.key === "Enter" && !e.shiftKey) {

                e.preventDefault();

                form.requestSubmit();

            }

        });

    }



    // ==========================================
    // Copy AI Answer
    // ==========================================

    if (copyBtn && answerText) {

        copyBtn.addEventListener("click", async () => {

            try {

                await navigator.clipboard.writeText(
                    answerText.innerText
                );

                copyBtn.innerHTML =
                    '<i class="fa-solid fa-check"></i> Copied!';

                copyBtn.style.background = "#16a34a";

                setTimeout(() => {

                    copyBtn.innerHTML =
                        '<i class="fa-regular fa-copy"></i> Copy';

                    copyBtn.style.background = "";

                }, 1800);

            }

            catch (err) {

                alert("Unable to copy.");

            }

        });

    }



    // ==========================================
    // Auto Scroll to Latest AI Message
    // ==========================================

    if (answerText) {

        setTimeout(() => {

            answerText.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        }, 350);

    }



    // ==========================================
    // Ripple Animation
    // ==========================================

    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {

        button.addEventListener("click", function (e) {

            const ripple = document.createElement("span");

            ripple.classList.add("ripple");

            const rect = this.getBoundingClientRect();

            ripple.style.left =
                `${e.clientX - rect.left}px`;

            ripple.style.top =
                `${e.clientY - rect.top}px`;

            this.appendChild(ripple);

            setTimeout(() => {

                ripple.remove();

            }, 600);

        });

    });



    // ==========================================
    // Textarea Auto Grow
    // ==========================================

    if (textarea) {

        textarea.addEventListener("input", function () {

            this.style.height = "auto";

            this.style.height = this.scrollHeight + "px";

        });

    }



    // ==========================================
    // Fade Buttons In
    // ==========================================

    const animatedButtons =
        document.querySelectorAll(
            ".video-btn, .dashboard-btn, .timestamp-pill"
        );

    animatedButtons.forEach((btn, index) => {

        btn.style.opacity = "0";

        btn.style.transform = "translateY(15px)";

        setTimeout(() => {

            btn.style.transition =
                "all .4s ease";

            btn.style.opacity = "1";

            btn.style.transform =
                "translateY(0px)";

        }, 120 * index);

    });



    // ==========================================
    // Timestamp Hover Effect
    // ==========================================

    const timestampButtons =
        document.querySelectorAll(".timestamp-pill");

    timestampButtons.forEach(button => {

        button.addEventListener("mouseenter", () => {

            button.style.transform = "translateY(-3px)";

        });

        button.addEventListener("mouseleave", () => {

            button.style.transform = "";

        });

    });



    // ==========================================
    // Prevent Double Submission
    // ==========================================

    const sendButton = document.getElementById("sendBtn");

    if (form && sendButton) {

        form.addEventListener("submit", () => {

            sendButton.disabled = true;

            sendButton.innerHTML =

                '<i class="fa-solid fa-spinner fa-spin"></i> Thinking...';

        });

    }

});