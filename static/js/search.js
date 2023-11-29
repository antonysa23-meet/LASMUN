const countries = document.querySelectorAll('li')
var starter = 0
for (i = 0; i < countries.length; ++i) {
    if ((countries[i].textContent.toLowerCase().includes('afghanistan'))){
        starter = i
        break
    }
}
console.log(starter)
function lookup(){

    var search = document.getElementById('search').value.toLowerCase();
    // console.log(countries[20])
    for (i = starter; i < starter + 140; ++i) {
        if (!(countries[i].textContent.toLowerCase().includes(search))){
            // console.log(search)
            // console.log(countries[i])
            countries[i].style.display = ('none');
        }
        else{
            countries[i].style.display = ('block');
        }
    }
    setTimeout(lookup, 300)
}
lookup()