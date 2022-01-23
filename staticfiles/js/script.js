mybutton = document.getElementById("myBtnn");

// When the user scrolls down 1000px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

const SubsciberLogic = {
	emailManager(email) {
		fetch('/api/subscriberapi/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				'email': email,
			})
		})
			.then(response => response.json())
			.then(data => {

			});
	}
}

emailbutton = document.getElementById('emailbutton')
emailinput = document.getElementById('emailinput')

emailbutton.onclick = function () {
    const email = emailinput.value;
    SubsciberLogic.emailManager(email);
}
