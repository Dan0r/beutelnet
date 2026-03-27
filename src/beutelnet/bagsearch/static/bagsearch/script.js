// Select elements in the DOM
const searchInput = document.getElementById("search-input");
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
searchInput.addEventListener('keyup', input=> {
	if (input.target.value.trim().length != 0) {
		sendInput(input.target.value)
	}
})

// Fetch data from view according to search-input
const sendInput = debounce(async (vacuum) => {
	try {
		const response = await fetch(`/get_data?search_term=${encodeURIComponent(vacuum)}`, {method: "GET",})

		if (!response.ok) {
			throw new Error(`Response status ${response.status}`);
		}

		const res = await response.json();
		// Go through each VacuumBag and add data to table
		renderTable(res);
	} catch (error) {
		console.log(error.message);
	}
}, 250);


// Render table with placeholders
function renderTable(res) {
	// Go through the Array res
	// Append each VacuumBag data
	const rows = res.map(vacuum => `
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
		</tr>
	`).join("");
	// Update table with the rows
	tableBody.innerHTML = rows;
}
