const copyBtn = document.getElementById("copyBtn");
const summaryText = document.getElementById("summaryText");

copyBtn.addEventListener("click", () => {

    navigator.clipboard.writeText(summaryText.innerText);

    copyBtn.innerHTML = "Copied ✓";

    setTimeout(() => {

        copyBtn.innerHTML = "Copy";

    },2000);

});