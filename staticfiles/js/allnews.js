function getAllNews(start, end, category) {
    fetch(`http://127.0.0.1:8000/api/newsapi?start=${start}&end=${end}&category=${category}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            news = document.getElementById('news');
            for (let i = 0; i < data.length; i++) {
                newsCounter += 1;
                news.children[0].innerHTML += `
                            ${newsCounter % 8 != 0 && newsCounter % 8 != 1 ? `
                            <div class="col-sm-4 my-3">
                                <div class="card" style="height: 100%">
                                    <a href="${data[i]['id']}"><img class="card-img-top" style="height: 284px;" src="${data[i].image}" alt="Card image cap"></a>` :
                        `<div class="col-sm-6 my-3">
                            <div class="card" style="height: 100%">
                            <a href="${data[i]['id']}"><img class="card-img-top" style="height: 440px;" src="${data[i]['image']}" alt="Card image cap"> </a>`}
                                <div class="card-body text-left">
                                    <p class="card-text">${data[i]['created_at']} | ${data[i]['category']['title']}</p>
                                    <p class="card-title">${data[i]['title']} </p>
                                    <p class="card-text">${data[i]['description']} </p>
                                </div>
                            </div>
                        </div>
            `;
            }
            if (start > 0) {
                window.scrollTo(0, news.scrollHeight);
            }
            if (data.length < end - start) {
                more_button.classList.add('d-none');
            } else {
                more_button.classList.remove('d-none');
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getAllNews(0, 8, 'Hamısı');
    newsCounter = -1;
});

filter_button = document.getElementById('filter-button');
more_button = document.getElementById('more-button');
more_button.addEventListener('click', (event) => {
    for (let i = 0; i < filter_button.children.length; i++) {
        if (filter_button.children[i].disabled) {
            category = filter_button.children[i].innerText;
        }
    }
    getAllNews(news.children[0].children.length, news.children[0].children.length + 8, category);
});


for (let i = 0; i < filter_button.children.length; i++) {
    filter_button.children[i].addEventListener('click', (event) => {
        for (let i = 0; i < filter_button.children.length; i++) {
            filter_button.children[i].classList.remove('btn-outline-primary');
            filter_button.children[i].disabled = false;
        }
        event.target.classList.add('btn-outline-primary');
        event.target.disabled = true;
        news = document.getElementById('news');
        news.children[0].innerHTML = '';
        getAllNews(0, 8, event.target.innerText);
        newsCounter = -1;
    });
}