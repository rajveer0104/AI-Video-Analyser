// ===============================
// DROPZONE FILE INPUTS
// ===============================

document.querySelectorAll(".dropzone").forEach(zone => {

    const input = zone.querySelector("input[type=file]");
    const filenameEl = zone.querySelector(".dz-filename");

    if (!input) return;

    const showFile = () => {
        if (input.files && input.files.length > 0) {
            filenameEl.textContent = input.files[0].name;
            zone.classList.add("has-file");
        } else {
            filenameEl.textContent = "";
            zone.classList.remove("has-file");
        }
    };

    input.addEventListener("change", showFile);

    ["dragenter", "dragover"].forEach(evt => {
        zone.addEventListener(evt, (e) => {
            e.preventDefault();
            zone.classList.add("drag-over");
        });
    });

    ["dragleave", "drop"].forEach(evt => {
        zone.addEventListener(evt, (e) => {
            e.preventDefault();
            zone.classList.remove("drag-over");
        });
    });

    zone.addEventListener("drop", (e) => {
        if (e.dataTransfer.files.length > 0) {
            input.files = e.dataTransfer.files;
            showFile();
        }
    });

});

// ===============================
// BUTTON RIPPLE EFFECT
// ===============================

document.querySelectorAll(".btn").forEach(button => {

    button.addEventListener("click", function (e) {

        const ripple = document.createElement("span");
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);

        ripple.style.width = ripple.style.height = size + "px";
        ripple.style.left = e.clientX - rect.left - size / 2 + "px";
        ripple.style.top = e.clientY - rect.top - size / 2 + "px";
        ripple.className = "ripple";

        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);

    });

});