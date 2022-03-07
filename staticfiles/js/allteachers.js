function getAllTeachers(start, end, search) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`/api/teacherapi?start=${start}&end=${end}&search=${search}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            teachers = document.getElementById('teachers');
            for (let i = 0; i < data.length; i++) {
                teachers.children[0].innerHTML += `<div class="col-12 col-md-6 col-lg-3 ">
                <div class="card my-2" style="height: 328px; border-radius: 20px;">
                <a data-bs-target="#teacher${data[i]['id']}" data-bs-toggle="modal" style="cursor: pointer; height: 100%">
                <img class="card-img-top" style="border-radius: 20px; height: 100%; object-fit: cover;"
                src="${data[i]['photo']}"
                alt="Card image">
                <div style="position: absolute; bottom: 0; padding: 20px; top: inherit;"
                class="card-img-overlay text-light text-left">
                <p class="card-text"
                style="font-weight: 500; font-size: 15px; line-height: 18px; letter-spacing: 0.15px; color: ${data[i]['text_color']};">
                ${data[i]['subject']['title']}</p>
                <h4 class="card-title" 
                style="font-weight: 600; font-size: 24px; line-height: 29px; color: ${data[i]['text_color']}; margin-bottom: 0 !important;">${data[i]['full_name']} 
                </h4>
                </div>
                </a>
                </div>
                </div>
                <div class="modal fade" id="teacher${data[i]['id']}" tabindex="-1" aria-labelledby="teacher${data[i]['id']}Label" aria-hidden="true">
                <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-body">
                <h5 class="modal-title" id="teacher${data[i]['id']}Label" style="display: none;"></h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close" style="z-index: 1; position: absolute; top: 20px; left: 20px;"></button>
                <div class="card" style="border-radius: 20px; border: none; position: relative;">
                <img class="card-img-top" style="height: 400px; border-top-left-radius: 20px; border-top-right-radius: 20px;"
                src="${data[i]['photo']}"
                alt="Card image">
                <div class="card-img-overlay text-light text-left">
                <div style="margin-top: 80%;"> 
                <p class="card-text"
                style="font-weight: 500; font-size: 15px; line-height: 18px; letter-spacing: 0.15px; color: ${data[i]['text_color']};">
                ${data[i]['subject']['title']}</p>
                <h4 class="card-title "
                style="font-weight: 600; font-size: 24px; line-height: 29px; color: ${data[i]['text_color']}; margin-bottom: 0 !important;">${data[i]['full_name']} 
                </h4>
                </div>
                </div>
                        <div class="card-body">
                            <h5 class="card-title" style="font-size: 20px; line-height: 28px; letter-spacing: 0.15px; color: rgba(0, 0, 0, 0.6);text-align: left;">${data[i]['description']}</h5>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>`;
            }
            spinner.classList.add('d-none');
            if (start > 0) {
                window.scrollTo(0, teachers.scrollHeight);
            }
            if (data.length < end - start) {
                more_button.classList.add('d-none');
            } else {
                more_button.classList.remove('d-none');
            }
        });
}

window.addEventListener('DOMContentLoaded', () => {
    getAllTeachers(0, 16, 'all');
});

search = document.getElementById('search');
search.addEventListener('keyup', (event) => {
    // len = teachers.children[0].children.length/2;
    teachers.children[0].innerHTML = '';
    getAllTeachers(0, 4, event.target.value);
    // getAllTeachers(0, len, event.target.value);
});
more_button = document.getElementById('more-button');
more_button.addEventListener('click', () => {
    getAllTeachers(teachers.children[0].children.length / 2, teachers.children[0].children.length / 2 + 4, search.value);
});