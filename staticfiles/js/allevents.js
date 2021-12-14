function getFutureEvents() {
    fetch(`http://127.0.0.1:8000/api/futureeventapi`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            event_carousel = document.getElementById('event-carousel');
            for (let i = 0; i < data.length / 2; i++) {
                event_carousel.innerHTML += `<div class="carousel-item"></div>`;
            }
            counter = 0;
            for (let i = 1; i < event_carousel.children.length; i++) {
                if (data[counter]) {
                    event_carousel.children[i].innerHTML += `<div class="col-md-6" style="float:left">
                    <div class="card mb-2">
                    <img class="card-img-top" style="border-radius: 24px; height: 312px;"
                    src="${data[counter]['image']}"
                    alt="Card image cap">
                    <div class="card-body">
                    <a class="btn"
                    style="padding: 3px 16px 5px; background: rgba(11, 82, 254, 0.12); border-radius: 100px; color: #0B52FE;">${data[counter]['category']['title']}</a>
                    <h4 class="card-title"
                    style="font-weight: 600; font-size: 24px; line-height: 32px; color: #000000; ">${data[counter]['title']}</h4>
                                <p class="card-text"
                                style="font-weight: 600; font-size: 15px; line-height: 24px; letter-spacing: 0.5px; text-transform: uppercase; color: rgba(0, 0, 0, 0.6); ">
                                ${data[counter]['date']}</p>
                                </div>
                                </div>
                                <hr style="background: rgba(0, 0, 0, 0.08); border-radius: 1px; ">
                                </div>`
                }
                if (data[counter + 1]) {
                    event_carousel.children[i].innerHTML += `<div class="col-md-6" style="float:left">
                                <div class="card mb-2">
                                <img class="card-img-top" style="border-radius: 24px; height: 312px;"
                                src="${data[counter + 1]['image']}"
                                alt="Card image cap">
                                <div class="card-body">
                                <a class="btn"
                                style="padding: 3px 16px 5px; background: rgba(11, 82, 254, 0.12); border-radius: 100px; color: #0B52FE;">${data[counter + 1]['category']['title']}</a>
                                <h4 class="card-title"
                                style="font-weight: 600; font-size: 24px; line-height: 32px; color: #000000; ">${data[counter + 1]['title']}</h4>
                                <p class="card-text"
                                style="font-weight: 600; font-size: 15px; line-height: 24px; letter-spacing: 0.5px; text-transform: uppercase; color: rgba(0, 0, 0, 0.6); ">
                                ${data[counter + 1]['date']}</p>
                                </div>
                                </div>
                                <hr style="background: rgba(0, 0, 0, 0.08); border-radius: 1px; ">
                                </div>`
                }
                counter += 2
            }
        });
}
function getRecentEvents(start, end) {
    spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    fetch(`http://127.0.0.1:8000/api/recenteventapi?start=${start}&end=${end}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            recent_events = document.getElementById('recent-events');
            for (let i = 0; i < data.length; i++) {
                recent_events.innerHTML += `
            <div class="card col-md-6 mb-3 px-4">
                <div class="row">
                    <div class="col-md-5">
                        <img src="${data[i]['image']}"
                            class="img-fluid rounded" alt="..." style="height: 152px;">
                    </div>
                    <div class="col-md-7">
                        <div class="card-body pt-0 pl-0">
                            <a class="btn"
                                style="padding: 3px 16px 5px; background: rgba(11, 82, 254, 0.12); border-radius: 100px; color: #0B52FE;">${data[i]['category']['title']}</a>
                            <a class="recent-event-title" href="">
                                <h5 class="card-title"
                                    style="font-weight: 600; font-size: 24px; line-height: 32px; color: #000000; ">${data[i]['title']}</h5>
                            </a>
                            <p class="card-text"
                                style="font-weight: 600; font-size: 15px; line-height: 24px; letter-spacing: 0.5px; text-transform: uppercase; color: rgba(0, 0, 0, 0.6); ">
                                ${data[i]['date']}</p>
                        </div>
                    </div>
                    </div>
                    <hr style="background: rgba(0, 0, 0, 0.08); border-radius: 1px;">
            </div>`
            }
            spinner.classList.add('d-none');
            if (start > 0) {
                window.scrollTo(0, recent_events.scrollHeight);
            }
            if (data.length < end - start) {
                more_button.classList.add('d-none');
            } else {
                more_button.classList.remove('d-none');
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getFutureEvents();
    getRecentEvents(0, 8);
});



more_button = document.getElementById('more-button');
more_button.addEventListener('click', (event) => {
    getRecentEvents(recent_events.children.length, recent_events.children.length + 8);
});
