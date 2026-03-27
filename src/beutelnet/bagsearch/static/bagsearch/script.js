// Select elements in the DOM
const searchInput = document.getElementById("search-input");


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
}, 100);

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

// Send search-input
searchInput.addEventListener('keyup', input=> {
	console.log(input.target.value)
	sendInput(input.target.value)
})


//	// 2. Table bauen
