console.log('girdim');

button = document.querySelector('#button1');
button2 = document.querySelector('#button2');

newsfetch = document.querySelector('#newsfetch');
blogfetch = document.querySelector('#blogfetch');

button.addEventListener('click', () => {
    console.log("hey newsapi");
    fetch("http://127.0.0.1:8000/api/newsapi/").then(
        response => response.json()
    ).then(responseJson => {
        responseJson.forEach(item => {
            let dom = document.createElement('div')
            dom.innerHTML += `
                <div class="card m-5" style="width: 18rem;">
                
                <div class="card-body">
                    <h5 class="card-title">${item['title']}</h5>
                    <p class="card-text">${item['description']}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                </div>
            `
            let dom = document.createElement('li')
            dom.innerHTML = item.name
            newsfetch.appendChild(dom)

        });
    })
});

button2.addEventListener('click', () => {
    console.log("hey blogapi");
    fetch("http://127.0.0.1:8000/api/blogapi/").then(
        response => response.json()
    ).then(responseJson => {
        responseJson.forEach(item => {
            let dom = document.createElement('div')
            dom.innerHTML += `
                <div class="card m-5" style="width: 18rem;">
                <img src="" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${item['title']}</h5>
                    <p class="card-text">${item['description']}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                </div>
            `
            console.log(item.title);
            blogfetch.appendChild(dom)
            
        });
    })
});

