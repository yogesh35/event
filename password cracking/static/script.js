document.addEventListener("DOMContentLoaded", function () {
    const message = document.getElementById("congrats");
    message.style.opacity = "0";
    setTimeout(() => {
        message.style.transition = "opacity 2s ease-in-out";
        message.style.opacity = "1";
    }, 500);
});
