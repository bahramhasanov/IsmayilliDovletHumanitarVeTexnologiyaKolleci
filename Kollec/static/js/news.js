<<<<<<< HEAD
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
});


>>>>>>> b8f6be5d832e5e66b967e65b95227a2a6770a278
