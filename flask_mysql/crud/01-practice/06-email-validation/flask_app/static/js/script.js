var elems = document.getElementsByClassName('confirmation');
    var confirmIt = function (e) {//this code comes from https://stackoverflow.com/questions/10462839/how-to-display-a-confirmation-dialog-when-clicking-an-a-link
        if (!confirm('Are you sure about that?')) e.preventDefault();
    };
    for (var i = 0, l = elems.length; i < l; i++) {
        elems[i].addEventListener('click', confirmIt, false);
    }

function deleto(element){
    element.remove();
}