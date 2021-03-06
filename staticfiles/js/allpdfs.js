function getAllPDFs(start, end, subject) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`/api/pdfapi?start=${start}&end=${end}&category=${subject}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            pdfs = document.getElementById('pdfs');
            for (let i = 0; i < data.length; i++) {
                pdfs.children[0].innerHTML += `
                <div class="col-lg-3 col-md-6 my-3">
                <div class="card text-center" style="background: #F9F9F9; border-radius: 20px; height: 100%; border: none;">
                <div class="card-body">
                <img style="width: 64px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/1200px-PDF_file_icon.svg.png" alt="">
                <a style="font-weight: 600; font-size: 20px; line-height: 28px; text-align: center; letter-spacing: 0.15px; color: #000000;" target="_blank" href="${data[i]['slug']}/show"><p data-toggle="tooltip" title="${data[i]['title']}" class="card-title text-dark">${data[i]['title'].substring(0, 10)}</p></a>
                <p class="card-text mb-5">${data[i]['size']} KB</p>
                <a target="_blank" href="${data[i]['slug']}/download" class="btn btn-primary-outline text-primary" style="position: absolute; left: 0; right: 0; bottom: 5%;"><i
                class="fas fa-arrow-down"></i>  Endir</a>
                </div>
                </div>
                </div>`;
            }
            spinner.classList.add('d-none');
            if (start > 0) {
                window.scrollTo(0, pdfs.scrollHeight);
            }
            if (data.length < end - start) {
                more_button.classList.add('d-none');
            } else {
                more_button.classList.remove('d-none');
            }
            $('[data-toggle="tooltip"]').tooltip();
        });
}

window.addEventListener('DOMContentLoaded', () => {
    getAllPDFs(0, 16, 'all');
});


more_button = document.getElementById('more-button');
more_button.addEventListener('click', () => {
    getAllPDFs(pdfs.children[0].children.length, pdfs.children[0].children.length + 8, input.value);
});



input = document.getElementById("subjects");
subjectDropdown = document.getElementById('subjectDropdown');

function filterFunction() {
    txtValue = input.value;
    if (txtValue != "") {
        getAllSubjects(txtValue);
    } else {
        subjectDropdown.innerHTML = '';
    }
}


function getAllSubjects(subject, type = null) {
    fetch(`/api/subjectapi?subject=${subject}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            subjectDropdown.innerHTML = '';
            if (data.length > 0) {
                // subjectDropdown.innerHTML += `<a class="dropdown-item" onclick="selectSubject(this)">B??t??n f??nnl??r</a>`;
                for (let i = 0; i < data.length; i++) {
                    if (data[i]['title'] != subject) {
                        subjectDropdown.innerHTML += `<a class="dropdown-item" onclick="selectSubject(this)">${data[i]['title']}</a>`;
                    }
                }
            } else {
                subjectDropdown.innerHTML = `<a class="dropdown-item disabled">Subject not found</a>`;
            }
            if (type == "getPDFs") {
                pdfs.children[0].innerHTML = '';
                getAllPDFs(0, 16, subject);
            }
        });
}

function selectSubject(d) {
    subject = d.innerText;
    input.value = subject;
    type = "getPDFs"
    getAllSubjects(subject, type);
}
