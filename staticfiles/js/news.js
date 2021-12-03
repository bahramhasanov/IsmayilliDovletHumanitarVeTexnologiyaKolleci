<<<<<<< HEAD

button = document.querySelector('#button1');
button2 = document.querySelector('#button2');

newsfetch = document.querySelector('.newsfetch');
blogfetch = document.querySelector('#blogfetch');


button.addEventListener('click', () => {
    fetch("http://127.0.0.1:8000/api/newsapi/").then(
        response => response.json()
    ).then(responseJson => {
        responseJson.forEach(item => {
            let dom = document.createElement('div');
            console.log(item.images[0].url);
            dom.innerHTML += `
            <div class="card m-5" style="width: 18rem;">
                <img src="${item.images[0]['url']}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${item['name']}</h5>
                    <h5 class="card-title">${item['subtitle']}</h5>
                    <p class="card-text">${item['description']}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                </div>
            `
            newsfetch.appendChild(dom)
        });
    })
=======
newsfetch = document.querySelector('#newsfetch');
fetch("http://127.0.0.1:8000/api/newsapi/").then(
    response => response.json()
).then(responseJson => {
    responseJson.forEach(item => {
        let dom = document.createElement('li')
        dom.innerHTML = item.name
        newsfetch.appendChild(dom)

    });
>>>>>>> b8f6be5d832e5e66b967e65b95227a2a6770a278
});

button2.addEventListener('click', () => {
    fetch("http://127.0.0.1:8000/api/blogapi/").then(
        response => response.json()
    ).then(responseJson => {
        console.log('heyy');
        responseJson.forEach(item => {
            let dom = document.createElement('div')
            dom.innerHTML += `
            <div class="card m-5" style="width: 18rem;">
            <img src="${item.images[0]['url']}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${item['title']}</h5>
                <p class="card-text">${item['description']}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
            </div>
            `
            console.log(item.images[0]['url']);
            blogfetch.appendChild(dom)
            
        });
    })
});

