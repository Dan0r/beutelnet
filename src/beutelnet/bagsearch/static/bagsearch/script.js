// Select elements in the DOM
const searchInput = document.getElementById("search-input");


// Debounce search-input for performance
function debounce(func, timeout = 300){
	let timer;
	return (...args) => {
		// Clear any previous timeout
		clearTimeout(timer);
		// Set timeout
		timer = setTimeout(() => { func.apply(this, args); }, timeout);
	};
}

// Fetch data from view
const sendInput = debounce(async (vacuum) => {
	try {
		const response = await fetch(`/get_data?search_term=${encodeURIComponent(vacuum)}`, {method: "GET",})

		if (!response.ok) {
			throw new Error(`Response status ${response.status}`);
		}

		const res = await response.json();
		console.log(res);
	} catch (error) {
		console.log(error.message);
	}
}, 250);


// Send search-input
searchInput.addEventListener('keyup', input=> {
	if (input.target.value.trim().length != 0) {
		console.log(input.target.value)
		sendInput(input.target.value)
	}
})

// Expand table
