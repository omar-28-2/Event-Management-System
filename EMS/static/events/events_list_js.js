document.getElementById("searchButton").addEventListener("click", function () {
    const searchValue = document.getElementById("searchBar").value.toLowerCase();
    const cards = document.querySelectorAll(".item-container");

    cards.forEach((card) => {
        const title = card.querySelector(".title").textContent.toLowerCase();
        const location = card.querySelector(".info").textContent.toLowerCase();
        const description = card.querySelector(".description") ? card.querySelector(".description").textContent.toLowerCase() : "";

        // Show the card if title, location or description matches the search value
        if (title.includes(searchValue) || location.includes(searchValue) || description.includes(searchValue)) {
            card.style.display = "flex"; // Show the card
        } else {
            card.style.display = "none"; // Hide the card
        }
    });
});
