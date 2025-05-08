// TODO: Change me if needed
const selector = "input[type='global-search']";

document.addEventListener("DOMContentLoaded", function(event) {
    // Trigger Read the Docs' search addon instead of the default search
    document.querySelector(selector).addEventListener("click", (e) => {
        const event = new CustomEvent("readthedocs-search-show");
        document.dispatchEvent(event);
    });
});
