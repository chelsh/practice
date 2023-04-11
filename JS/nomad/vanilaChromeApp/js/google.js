const srchForm = document.querySelector("#srch-form");
const srchInput = document.querySelector("srch-form input");

srchInput.addEventListener("submit", onSearchSubmit);

function onSearchSubmit(event) {
  event.preventDefault();
  const searchWord = srchInput.value;
  window.open("https://www.google.com/search?q=" + searchWord);
}
