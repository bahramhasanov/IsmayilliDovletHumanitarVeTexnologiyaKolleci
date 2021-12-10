
function getAllPDFs(start, end, subject) {
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
                pdfs.children[0].innerHTML += `<div class="col-lg-3 col-md-6 my-3">
                <div class="card text-center" style="background: #F9F9F9; border-radius: 20px;">
                <div class="card-body">
                    <img style="width: 64px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/1200px-PDF_file_icon.svg.png" alt="">
                    <p class="card-title">${data[i]['title']}</p>
                    <p class="card-text">${data[i]['size']}</p>
                    <a href="${data[i]['id']}" class="btn btn-outline-primary"><i
                            class="fas fa-arrow-down"></i>Endir</a>
                </div>
            </div>
        </div>`;
            }
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
    getAllPDFs(0, 4, 'all');
});

more_button = document.getElementById('more-button');
more_button.addEventListener('click', () => {
    getAllPDFs(pdfs.children[0].children.length, pdfs.children[0].children.length + 4, input.value);
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



function getAllSubjects(subject) {
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
            for (let i = 0; i < data.length; i++) {
                subjectDropdown.innerHTML += `<a class="dropdown-item" onclick="selectSubject(this)">${data[i]['title']}</a>`;
            }
            getAllPDFs(0, 4, subject);
            pdfs.children[0].innerHTML = '';
        });
}

function selectSubject(d) {
    subject = d.innerText;
    input.value = subject;
    getAllSubjects(subject);
}
