document.addEventListener("DOMContentLoaded", function() {
    // Inițializare dropdown-uri Bootstrap
    document.querySelectorAll('.dropdown-toggle').forEach(function (dropdown) {
        new bootstrap.Dropdown(dropdown);
    });

    // Imagine: deschide modal
    var imageModal = document.getElementById('imageModal');
    if (imageModal) {
        imageModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget;
            var imageUrl = button.getAttribute('data-bs-image');
            var title = button.getAttribute('data-bs-title');

            var modalImage = document.getElementById('modalImage');
            var modalTitle = document.getElementById('imageModalLabel');

            modalImage.src = imageUrl;
            modalTitle.textContent = title;
        });
    }

    // Ștergere media
    document.querySelectorAll('.delete-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var itemId = this.getAttribute('data-id');
            if (!itemId || isNaN(itemId) || parseInt(itemId) <= 0) {
                alert('ID-ul media nu este valid.');
                return;
            }
            var form = document.getElementById("confirmDeleteForm");
            form.action = "/delete_media/" + itemId + "/";
        });
    });
});
