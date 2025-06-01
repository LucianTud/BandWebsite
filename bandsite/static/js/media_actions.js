document.addEventListener("DOMContentLoaded", function () {
    // Inițializare dropdown-uri Bootstrap
    document.querySelectorAll('.dropdown-toggle').forEach(function (dropdown) {
        new bootstrap.Dropdown(dropdown);
    });

    // Funcționalitate admin: toggle zi disponibilă/indisponibilă în calendar
    const calendarEl = document.getElementById("calendar");
    if (calendarEl && calendarEl.dataset.isStaff === "true") {
        calendarEl.addEventListener("click", function (event) {
            // Detectăm clic pe zi
            const dateEl = event.target.closest(".fc-daygrid-day");
            if (dateEl) {
                const date = dateEl.getAttribute("data-date");
                if (!date) return;

                // Confirmare opțională
                const confirmToggle = confirm(`Vrei să modifici disponibilitatea pentru ${date}?`);
                if (!confirmToggle) return;

                // Trimitere request
                fetch("/calendar/toggle/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                    body: JSON.stringify({ date: date }),
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "added" || data.status === "removed") {
                        location.reload(); // Reîncărcăm calendarul
                    } else {
                        alert("Eroare: " + data.message);
                    }
                })
                .catch(error => {
                    console.error("Eroare la toggle disponibilitate:", error);
                    alert("A apărut o eroare. Încearcă din nou.");
                });
            }
        });
    }

    // Utilitar: obține CSRF din cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
