const brightness = document.querySelector('#brightness');

fetch('get-brightness')
    .then(response => response.text())
    .then(text => brightness.innerHTML = text);

setInterval(() => {
    fetch('get-brightness')
        .then(response => response.text())
        .then(text => brightness.innerHTML = text);
}, 10000)