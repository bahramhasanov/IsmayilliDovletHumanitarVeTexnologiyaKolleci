// $(document).ready(function () {


//     $('.owl-carousel').owlCarousel({
//         mouseDrag: true,
//         touchDrag: true,
//         loop: true,
//         // margin: -300,
//         nav: true,
//         navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
//         dots: false,
//         responsive: {
//             0: {
//                 items: 1
//             },
//             800: {
//                 items: 3
//             },
//             1000: {
//                 items: 5
//             }
//         }
//     });

//     $('.owl-prev').click(function () {
//         $active = $('.owl-item .item.show');
//         $('.owl-item .item.show').removeClass('show');
//         $('.owl-item .item').removeClass('next');
//         $('.owl-item .item').removeClass('prev');
//         $active.addClass('next');
//         $items = $('.owl-item .item');
//         if ($active.is('.first')) {
//             $('.owl-item .last').addClass('show');
//             $('.first').addClass('next');
//             $('.owl-item .last').parent().prev().children('.item').addClass('prev');
//         }
//         else {
//             $active.parent().prev().children('.item').addClass('show');
//             if ($active.parent().prev().children('.item').is('.first')) {
//                 $('.owl-item .last').addClass('prev');
//                 $firsts = $('.owl-item .item.first')
//                 $firsts.removeClass('prev');
//                 $firsts.addClass('show');
//             }
//             else {
//                 $('.owl-item .show').parent().prev().children('.item').addClass('prev');
//             }
//         }
//         $items.each(function () {
//             if ($(this).is('.show')) {
//                 $(this).removeClass('prev');
//             }
//             else {
//                 $(this).addClass('prev');
//             }
//         });
//         $('.item').removeClass('sides');
//         $('.owl-item .item.show').parent().prev().prev().each(function () {
//             if ($(this).is('.active')) {
//                 $(this).children('.item').addClass('sides');
//             }
//         });
//         $('.owl-item .item.show').parent().next().next().each(function () {
//             if ($(this).is('.active')) {
//                 $(this).children('.item').addClass('sides');
//             }
//         });
//     });

//     $('.owl-next').click(function () {
//         $active = $('.owl-item .item.show');
//         $('.owl-item .item.show').removeClass('show');
//         $('.owl-item .item').removeClass('next');
//         $('.owl-item .item').removeClass('prev');
//         $('.owl-item .item').addClass('prev');
//         $active.addClass('prev');
//         if ($active.is('.last')) {
//             $('.owl-item .first').addClass('show');
//             $('.owl-item .first').parent().next().children('.item').addClass('prev');
//         }
//         else {
//             $active.parent().next().children('.item').addClass('show');
//             if ($active.parent().next().children('.item').is('.last')) {
//                 $('.owl-item .first').addClass('next');
//             }
//             else {
//                 $('.owl-item .show').parent().next().children('.item').addClass('next');
//             }
//         }
//         $('.owl-item .item.show').removeClass('prev');
//         $('.item').removeClass('sides');
//         $('.owl-item .item.show').parent().prev().prev().each(function () {
//             if ($(this).is('.active')) {
//                 $(this).children('.item').addClass('sides');
//             }
//         });
//         $('.owl-item .item.show').parent().next().next().each(function () {
//             if ($(this).is('.active')) {
//                 $(this).children('.item').addClass('sides');
//             }
//         });
//     });
// });



$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        center: true,
        mouseDrag: true,
        touchDrag: true,
        autoplay: true,
        autoplayTimeout: 3000,
        keyboard: true,
        autoplayHoverPause: true,
        loop: true,
        margin: 2,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
    $('*').on('load', function () {
        console.log('event');
        var items = document.querySelectorAll('.owl-stage .active');
        for (let i = 0; i < items.length; i++) {
            items[i].children[0].classList.remove('sides');
            items[i].children[0].classList.remove('beforeSides');
            if (items[i].classList.contains('center') == false) {
                if (i == 0 | i == 4) {
                    items[i].children[0].classList.add('sides');
                } else if (i == 1 | i == 3) {
                    items[i].children[0].classList.add('beforeSides');
                }
            }
        }
    })

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