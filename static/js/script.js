document.addEventListener("DOMContentLoaded", function () {

    // 1. Mobile sidebar
    const menuButton = document.getElementById("mobileMenuBtn");
    const sidebar = document.getElementById("sidebar");

    if (menuButton && sidebar) {
        menuButton.addEventListener("click", function () {
            sidebar.classList.toggle("open");
        });
    }

    // 2. Delete confirmation
    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = window.confirm(
                "Are you sure you want to delete this student?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // 3. Auto-hide success messages
    const messages = document.querySelectorAll(".message");

    messages.forEach(function (message) {
        if (!message.classList.contains("error")) {
            setTimeout(function () {
                message.style.opacity = "0";

                setTimeout(function () {
                    message.remove();
                }, 300);

            }, 4000);
        }
    });

    // 4. Quick-search: press Enter to submit
    const quickSearch = document.querySelector(".quick-search input");

    if (quickSearch) {
        quickSearch.addEventListener("keydown", function (event) {
            if (event.key === "Enter") {
                this.form.submit();
            }
        });
    }
});
