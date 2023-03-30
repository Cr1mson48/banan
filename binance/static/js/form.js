const showPwdBtns = document.querySelectorAll("button[data-attr-show-pwd]");

Array.from(showPwdBtns).forEach((btn) => {
  btn.addEventListener("click", (event) => {
    const input = event.target.closest(".input").querySelector("input");
    const state = btn.getAttribute("data-attr-show-pwd") === "true";
    input.type = state ? "password" : "text";
    console.log(state);
    btn.setAttribute("data-attr-show-pwd", !state);
  });
});
