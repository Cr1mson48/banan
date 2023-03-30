function throttle(callee, timeout = 100) {
  let timer = null;
  return function perform(...args) {
    if (timer) return;
    timer = setTimeout(() => {
      callee(...args);
      clearTimeout(timer);
      timer = null;
    }, timeout);
  };
}

//DROPDOWN
const dropdown = document.getElementById("dropdown");
const dropdownList = document.getElementById("dropdown-list");
let isDropdownOpen = false;

function openDropdown() {
  updDropdownListPosition();
  dropdownList.style.visibility = "visible";
  dropdown.classList.add("is-open");
}

function closeDropdown() {
  dropdownList.style.visibility = "hidden";
  dropdown.classList.remove("is-open");
}

function setupDropdown() {
  dropdown.addEventListener("click", () => {
    isDropdownOpen = !isDropdownOpen;

    if (isDropdownOpen) {
      openDropdown();
    } else {
      closeDropdown();
    }
  });

  dropdownList.addEventListener("click", () => {
    isDropdownOpen = false;
    closeDropdown();
  });
}

function updDropdownListPosition() {
  const { left, height, top, width } = dropdown.getBoundingClientRect();

  dropdownList.style.top = `${top + height + 4}px`;
  dropdownList.style.left = `${left}px`;
  dropdownList.style.width = `${width}px`;
}

const updateVH = () => {
  const height = `${window.visualViewport.height}px`;
  document.documentElement.style.setProperty("--screen-height", height);
};

window.addEventListener(
  "resize",
  throttle(() => {
    updateVH();
    updDropdownListPosition();
  })
);

setupDropdown();
updateVH();
