// const copyText = document.querySelector("#copyMe")
// const showText = document.querySelector("p")

// const copyMeOnClipboard = () => {
//   copyText.select()
//   copyText.setSelectionRange(0, 99999) // used for mobile phone
//   document.execCommand("copy")
//   showText.innerHTML = `${copyText.value} is copied`
//   setTimeout(() => {
//     showText.innerHTML = ""
//   }, 1000)
// }

const copy = (element) => {
  document.getElementById(element).select();
  document.execCommand("copy");
}
  



const openEls = document.querySelectorAll("[data-open]");
const closeEls = document.querySelectorAll("[data-close]");
const isVisible = "is-visible";

for (const el of openEls) {
  el.addEventListener("click", function() {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  });
}

for (const el of closeEls) {
  el.addEventListener("click", function() {
    this.parentElement.parentElement.parentElement.classList.remove(isVisible);
  });
}

document.addEventListener("click", e => {
  if (e.target == document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});

document.addEventListener("keyup", e => {
  // if we press the ESC
  if (e.key == "Escape" && document.querySelector(".modal.is-visible")) {
    document.querySelector(".modal.is-visible").classList.remove(isVisible);
  }
});


