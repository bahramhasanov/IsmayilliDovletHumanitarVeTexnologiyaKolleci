function getAllNews(start, end, category) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`/api/newsapi?start=${start}&end=${end}&category=${category}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            news = document.getElementById('news');
            for (let i = 0; i < data.length; i++) {
                newsCounter += 1;
                news.children[0].innerHTML += `
                ${newsCounter % 8 != 0 && newsCounter % 8 != 1 ? `
                <div class="col-sm-4 my-3">
                <div class="card" style="height: 100%; border-radius: 20px;">
                <a href="${data[i]['slug']}"><img class="card-img-top" style="height: 240px; border-top-left-radius: 20px; border-top-right-radius: 20px;" src="${data[i].image}" alt="Card image cap"></a>` :
                        `<div class="col-sm-6 my-3">
                <div class="card" style="height: 100%; border-radius: 20px;">
                <a href="${data[i]['slug']}"><img class="card-img-top" style="height: 240px; border-top-left-radius: 20px; border-top-right-radius: 20px;" src="${data[i]['image']}" alt="Card image cap"> </a>`}
                <div class="card-body text-left">
                <p class="card-text" style="color: rgba(0, 0, 0, 0.6);">${data[i]['created_at']} | ${data[i]['category']['title']}</p>
                <p class="card-title" style="font-weight: 600; font-size: 24px; line-height: 32px; color: #000000;">${data[i]['title']} </p>
                <p class="card-text" style="font-size: 17px; line-height: 24px; letter-spacing: 0.15px; color: rgba(0, 0, 0, 0.6);
                ">${data[i]['description'].substring(0, 500)}</p>
                </div>
                            </div>
                            </div>
                            `;
            }
            spinner.classList.add('d-none');
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