scrollTopicon = document.getElementById("scrollTopicon");

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

    // scrollTopicon.addEventListener("mouseover", function() {
    //     faarrowcircleup.style.color = "red";
    // });
}