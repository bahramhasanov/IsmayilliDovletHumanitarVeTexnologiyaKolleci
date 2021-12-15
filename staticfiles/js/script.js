scrollTopicon = document.getElementById("scrollTopicon");

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera

}

const SubsciberLogic = {
	emailManager(email) {
		fetch('http://127.0.0.1:8000/api/subscriberapi/', {
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
