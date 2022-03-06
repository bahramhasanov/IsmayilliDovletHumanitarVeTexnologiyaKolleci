function getAllGallery(start, end, search='') {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`/api/galleryapi?start=${start}&end=${end}&search=${search}`, {
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



window.addEventListener('DOMContentLoaded', () => {
    getAllGallery(0, 16);
});

search = document.getElementById('search');
search.addEventListener('keyup', (event) => {
    gallery.innerHTML = '';
    getAllGallery(0, 4, event.target.value);

});
more_button = document.getElementById('more-button');
more_button.addEventListener('click', () => {
    getAllGallery(gallery.children.length, gallery.children.length + 4, search.value);

});