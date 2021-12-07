function getAllNews(start, end, category) {
    fetch('http://127.0.0.1:8000/api/newsapi', {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
                if (category != 'Hamısı') {
                    data = data.filter(item => item.category.title == category);
                }
                slicedData = data.slice(start, end);
                news = document.getElementById('news');
                for (let i = 0; i < slicedData.length; i++) {
                    newsCounter += 1;
                    news.children[0].innerHTML += `
                            ${newsCounter % 8 != 0 && newsCounter % 8 != 1 ? `
                            <div class="col-sm-4 my-3">
                                <div class="card">
                                    <a href="${slicedData[i]['id']}"><img class="card-img-top" style="height: 284px;" src="${slicedData[i].image}" alt="Card image cap"></a>` :
                        `<div class="col-sm-6 my-3">
                            <div class="card">
                            <a href="${slicedData[i]['id']}"><img class="card-img-top" style="height: 440px;" src="${slicedData[i]['image']}" alt="Card image cap"> </a>`}
                                <div class="card-body text-left">
                                    <p class="card-text">${slicedData[i]['created_at']} | ${slicedData[i]['category']['title']}</p>
                                    <p class="card-title">${slicedData[i]['title']} </p>
                                    <p class="card-text">${slicedData[i]['description']} </p>
                                </div>
                            </div>
                        </div>
            `;
            }
            if (start > 0) {
                window.scrollTo(0, news.scrollHeight);
            }

            if (news.children[0].children.length == data.length) {
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

more_button = document.getElementById('more-button');
more_button.addEventListener('click', (event) => {
    getAllNews(news.children[0].children.length, news.children[0].children.length + 5, 'Təhsil');
});

filter_button = document.getElementById('filter-button');

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