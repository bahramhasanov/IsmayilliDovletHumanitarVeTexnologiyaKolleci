
function getAllPDFs(start, end, subject) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`http://127.0.0.1:8000/api/pdfapi?start=${start}&end=${end}&category=${subject}`, {
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
                <div class="card text-center" style="background: #F9F9F9; border-radius: 20px; height: 100%">
                <div class="card-body">
                <img style="width: 64px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/1200px-PDF_file_icon.svg.png" alt="">
                <a href="${data[i]['id']}/show"><p class="card-title text-dark">${data[i]['title']}</p></a>
                <p class="card-text">${data[i]['category']['title']}</p>
                <a href="${data[i]['id']}/download" class="btn btn-outline-primary"><i
                class="fas fa-arrow-down"></i>Endir</a>
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
    fetch(`http://127.0.0.1:8000/api/subjectapi?subject=${subject}`, {
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
