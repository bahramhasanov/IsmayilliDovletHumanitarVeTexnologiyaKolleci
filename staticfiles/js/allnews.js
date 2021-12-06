
function getAllNews(start, end) {
    fetch('http://127.0.0.1:8000/api/newsapi', {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
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
            if (news.children[0].children.length == data.length) {
                more_button.style.display = 'none';
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getAllNews(0, 13)
    newsCounter = -1;
});

more_button = document.getElementById('more-button');
more_button.addEventListener('click', (event) => {
    console.log(news.children[0].children.length);
    getAllNews(news.children[0].children.length, news.children[0].children.length + 1);
});