class Search {
	constructor(form, display_result) {
		/* Define the form, the search input and the list where to display result */
		this.form = form;
		this.input = this.form.querySelector("#id_name");
		this.display_result = document.getElementById(display_result);
		this.results = this.display_result.getElementsByTagName("li");

		/* Define all events listener */
		this.form.name.addEventListener("keyup", () => { this.process() });

		/* Limit time response for fectch */
		this.HttpHeaders = new Headers();
		this.HttpHeaders.append("Keep-Alive", "timeout=5");
	}

	process() {
		/* Find and display products'names */
		if (this.form.name.value.length < 3) {
			/* Avoid autocompletion for words under 2 letter */
			this.clear_result();
		} else {
			let formData = new FormData(this.form);
			fetch(auto_completion_url, {
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
				this.update_results();
			})
			.catch(error => console.log(error));
		}
	}

	clear_result() {
		/* Clear the displayed list */
		this.display_result.innerHTML = "";
		this.display_result.classList.add("hidden");
	}

	update_results() {
		this.results = this.display_result.getElementsByTagName("li");
		if (this.results.length > 0) {
			for (let i in this.results) {
				this.results.item(i).addEventListener("click", event => {
					this.form.name.value = event.target.textContent;
					this.clear_result();
					this.form.submit();
				});
			}
		}
	}
}

window.addEventListener("load", () => {
	let search_main_form = document.getElementById("search_main");
	if (search_main_form != null) {
		new Search(search_main_form, "results_main");
	}

	let search_short_form = document.getElementById("search_short");
	if (search_short_form != null) {
		new Search(search_short_form, "results_short");
	}
});
