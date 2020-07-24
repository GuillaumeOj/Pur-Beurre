class Search {
	constructor(form, display_result) {
		/* Define the form, the search input and the list where to display result */
		this.form = form;
		this.input = this.form.querySelector("#id_name");
		this.display_result = document.getElementById(display_result);

		/* Define all events listener */
		this.form.name.addEventListener("keyup", () => { this.process() });
		this.form.name.addEventListener("focusout", () => { this.clear_result() });

		/* Limit time response for fectch */
		this.HttpHeaders = new Headers();
		this.HttpHeaders.append("Keep-Alive", "timeout=5");
	}

	process() {
		/* Find and display products'names */
		if (this.form.name.value.length < 2) {
			/* Avoid autocompletion for words under 2 letter */
			this.clear_result();
		} else {
			let formData = new FormData(this.form);
			fetch(auto_find_url, {
				method: "POST",
				body: formData,
				headers: this.HttpHeaders
			})
			.then(response => {
				let status_code = response.status;
				if (status_code < 300) {
					return response.json();
				} else {
					throw new Error("Fatal error");
				}
			})
			.then(result =>  {
				this.clear_result();
				if ("products_names" in result) {
					if (result["products_names"].length > 0) {
						/* Display products' names */
						this.display_result.classList.remove("hidden");
						for (let i in result["products_names"]) {
							this.display_result.innerHTML += "<li>" + result["products_names"][i] + "</li>";
						}
					}
				}
			})
			.catch(error => console.log(error));
		}
	}

	clear_result() {
		/* Clear the displayed list */
		this.display_result.innerHTML = "";
		this.display_result.classList.add("hidden");
	}
}

let search_main_form = document.getElementById("search_main");
new Search(search_main_form, "results_main");

let search_short_form = document.getElementById("search_short");
new Search(search_short_form, "results_short");
