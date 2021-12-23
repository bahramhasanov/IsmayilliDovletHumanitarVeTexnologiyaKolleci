function getAllGallery(start, end, search) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`http://127.0.0.1:8000/api/galleryapi?start=${start}&end=${end}&search=${search}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            gallery = document.getElementById('gallery');
            for (let i = 0; i < data.length; i++) {
                gallery.innerHTML += `
                <div class="gallery card">
                <img class="card-img-top" src="${data[i]['image']}" alt="Card image cap">  
                </div>
            `;
            }
            spinner.classList.add('d-none');
            if (start > 0) {
                window.scrollTo(0, gallery.scrollHeight);
            }
            if (data.length < end - start) {
                more_button.classList.add('d-none');
            } else {
                more_button.classList.remove('d-none');
            }
        });
}


// *******************************************************

window.addEventListener('DOMContentLoaded', () => {
    getAllGallery(0, 16, 'all');
});

search = document.getElementById('search');
search.addEventListener('keyup', (event) => {
    gallery.innerHTML = '';
    console.log(event.target.value);
    getAllGallery(0, 4, event.target.value);

});
more_button = document.getElementById('more-button');
more_button.addEventListener('click', () => {
    console.log(gallery.children.length);
<<<<<<< HEAD
    getAllGallery(gallery.children.length , gallery.children.length + 4, search.value);

});
// *******************************************************

=======
    getAllGallery(gallery.children.length, gallery.children.length + 4, search.value);

});
// *******************************************************
>>>>>>> 235804bbba80b3d81008aa5a5db2cec6f6c96a37
