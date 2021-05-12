window.onload = function() {
  display();
};
function display(){
let divs = document.getElementsByClassName('display');

for (let x = 0; x < divs.length; x++) {
    let div = divs[x];
    let content = div.innerHTML.trim();

    if (content == 'None None' || content == 'None None') {
        div.style.display = 'none';
    }
}}

function goBack() {
  window.history.back();
}
