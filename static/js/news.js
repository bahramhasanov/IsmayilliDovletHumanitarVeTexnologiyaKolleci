button = document.querySelector('#button1');
button2 = document.querySelector('#button2');

newsfetch = document.querySelector('#newsfetch');
blogfetch = document.querySelector('#blogfetch');
console.log('girdim 1');
button.addEventListener('click', () => {
    console.log("hey newsapi");
    fetch("http://127.0.0.1:8000/api/newsapi/").then(
        response => response.json()
    ).then(responseJson => {
        responseJson.forEach(item => {
            console.log('girdim');
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



