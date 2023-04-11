const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("#login-form input");
const loginGreeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden";
const USERNAME = "username";

function paintGreetings(name) {
  loginGreeting.innerText = `Hello ${name}`;
  loginGreeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME);

if (savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  paintGreetings(savedUsername);
}

function onLoginSubmit(event) {
  event.preventDefault();
  username = loginInput.value;
  loginForm.classList.add(HIDDEN_CLASSNAME);
  paintGreetings(username);
  localStorage.setItem(USERNAME, username);
}
