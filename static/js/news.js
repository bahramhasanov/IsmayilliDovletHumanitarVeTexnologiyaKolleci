newsfetch = document.querySelector('#newsfetch');
fetch("http://127.0.0.1:8000/api/newsapi/").then(
    response => response.json()
).then(responseJson => {
    responseJson.forEach(item => {
        let dom = document.createElement('li')
        dom.innerHTML = item.name
        newsfetch.appendChild(dom)
        
    });
});


