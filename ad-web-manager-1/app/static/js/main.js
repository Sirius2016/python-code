document.addEventListener('DOMContentLoaded', function() {
    const addUserForm = document.getElementById('addUserForm');
    const deleteUserForm = document.getElementById('deleteUserForm');
    const batchAddForm = document.getElementById('batchAddForm');
    const batchDeleteForm = document.getElementById('batchDeleteForm');

    if (addUserForm) {
        addUserForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(addUserForm);
            fetch('/add_user', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                addUserForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (deleteUserForm) {
        deleteUserForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(deleteUserForm);
            fetch('/delete_user', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                deleteUserForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (batchAddForm) {
        batchAddForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(batchAddForm);
            fetch('/batch_add', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                batchAddForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (batchDeleteForm) {
        batchDeleteForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(batchDeleteForm);
            fetch('/batch_delete', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                batchDeleteForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }
});