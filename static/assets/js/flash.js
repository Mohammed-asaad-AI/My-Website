document.addEventListener("DOMContentLoaded", function () {
    const flash = document.querySelector(".custom-flash");
    if (flash) {
        flash.style.display = "block";
        setTimeout(() => {
            flash.style.opacity = "1";
        }, 100);
        setTimeout(() => {
            flash.style.opacity = "0";
            setTimeout(() => { flash.remove(); }, 1000);
        }, 4000);
    }
});
