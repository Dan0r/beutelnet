// Select elements in the DOM
const searchInput = document.getElementById("search-input");
const table = document.getElementById("table");
const tableBody = document.getElementById("table-body");


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
searchInput.addEventListener('keyup', userInput=> {
	// If input empty render an empty table
	if (userInput.target.value.trim().length === 0) {
		renderTable(userInput.target.value, [])
		return;
	} else {
		sendInput(userInput.target.value)
	}
})

// Fetch data from view according to search-input
const sendInput = debounce(async (userInput) => {
	try {
		const response = await fetch(`/get_data?search_term=${encodeURIComponent(userInput)}`, {method: "GET",})

		if (!response.ok) {
			throw new Error(`Response status ${response.status}`);
		}

		const res = await response.json();
		console.log(res);
		renderTable(userInput, res);
		// Go through each VacuumBag and add data to table
	} catch (error) {
		console.log(error.message);
	}
}, 250);


// Render table with placeholders
function renderTable(userInput, res) {
	let rows;
	// Hide table if no data for query OR no text in searchbar
	if (res.length === 0 || userInput.trim().length === 0) {
		table.classList.add('not-visible');
		tableBody.innerHTML = "";
		return;
		//rows =  `
		//	<tr align="center"> Entschuldigung: Modell nicht gefunden </tr>
		//`
	} else {
		table.classList.remove('not-visible');
		rows = res.map(vacuum => `
			<tr>
				<td>${vacuum.supermarket}</td>
				<td>${vacuum.vacuum}</td>
				<td>
				<svg width="50" height="50">
				<circle
				class="purple-circle"
				cx="25"
				cy="25"
				r="15">
				</circle>
				<text
				x="25"
				y="25"
				text-anchor="middle"
				dominant-baseline="middle"
				fill="white">
				${vacuum.size}</text>
				</svg>
				</td>
			</tr>`).join("");
	}
	// Update table with the rows
	tableBody.innerHTML = rows;
}
