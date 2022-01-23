$(document).ready(function () {

    $('.owl-carousel').owlCarousel({
        mouseDrag: false,
        loop: true,
        margin: 2,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 3
            }
        }
    });

    $('.owl-prev').click(function () {
        $active = $('.owl-item .item.show');
        $('.owl-item .item.show').removeClass('show');
        $('.owl-item .item').removeClass('next');
        $('.owl-item .item').removeClass('prev');
        $active.addClass('next');
        if ($active.is('.first')) {
            $('.owl-item .last').addClass('show');
            $('.first').addClass('next');
            $('.owl-item .last').parent().prev().children('.item').addClass('prev');
        }
        else {
            $active.parent().prev().children('.item').addClass('show');
            if ($active.parent().prev().children('.item').is('.first')) {
                $('.owl-item .last').addClass('prev');
            }
            else {
                $('.owl-item .show').parent().prev().children('.item').addClass('prev');
            }
        }
    });

    $('.owl-next').click(function () {
        $active = $('.owl-item .item.show');
        $('.owl-item .item.show').removeClass('show');
        $('.owl-item .item').removeClass('next');
        $('.owl-item .item').removeClass('prev');
        $active.addClass('prev');
        if ($active.is('.last')) {
            $('.owl-item .first').addClass('show');
            $('.owl-item .first').parent().next().children('.item').addClass('prev');
        }
        else {
            $active.parent().next().children('.item').addClass('show');
            if ($active.parent().next().children('.item').is('.last')) {
                $('.owl-item .first').addClass('next');
            }
            else {
                $('.owl-item .show').parent().next().children('.item').addClass('next');
            }
        }
    });

});


// function getTestimonial(){
//     fetch(`/api/testmonial`, {
//         method: 'GET',
//         credentials: 'include',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         testimonail = document.getElementById('testimonial');
//         for (let i = 0; i < data.length; i++) {
//             news.children[0].innerHTML += `
//             pass `;
//         }
// }

function getTestimonial() {
    fetch(`http://127.0.0.1:8000/api/testmonial`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            testimonail = document.getElementById('testimonial');
            for (let i = 0; i < data.length; i++) {
                // testimonailCounter += 1;
                testimonail.innerHTML += `
            <div class="student-card card col-md-3 my-sm-3 " style="padding: 2rem; background-color: #f6f6f6; border-radius: 20px; border: none;">
                <div class="card-content ">

                    <div class="p-0">
                        <div style="display: flex;">
                            <div class="profile "> <img src="${data[i]['image']}">
                            </div>
                            <div class="card-title " style="margin-left: 1rem; "> <span style="font-size: 19px; font-weight: 500px; line-height: 23px;">${data[i]['name']} <br>
                                    Nihal</span><br /> <span style="text-transform: uppercase; font-size: 13px; opacity: 0.6;">${data[i]['status']}</span>
                            </div>
                        </div>
                        <div class="card-subtitle " style="margin-top: 1.5rem;">
                            <p style="margin-bottom: 0 !important; font-size: 20px; line-height: 28px; font-weight: 400px;">
                            ${data[i]['description']}
                            </p>
                        </div>
                    </div>
                    <div>
                        <span class="fa fa-star "></span>
                        <span class="fa fa-star "></span>
                        <span class="fa fa-star "></span>
                        <span class="fa fa-star "></span>
                        <span class="fa fa-star "></span>
                    </div>
                </div>
            </div> `;
            }
        });
}