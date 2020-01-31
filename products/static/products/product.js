var formLabel = document.querySelector("body > div > div > main > div > div > div.products-content > div.product-detail-comments > form > div > label")
var formText = document.querySelector('textarea');
formLabel.classList.add("mdl-textfield__label");
formText.classList.add("mdl-textfield__input");
formText.setAttribute('type', 'text');
formText.setAttribute('rows', '0');
