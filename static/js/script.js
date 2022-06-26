document.getElementById("copy-right").innerHTML = new Date().getFullYear();

let edit = document.getElementById('edit-btn');
edit.addEventListener('click', editToggle)

function editToggle(){
    if (edit.innerText == 'CANCEL EDIT') {
        edit.innerText = 'EDIT PROFILE'
    } else {
        edit.innerText = 'CANCEL EDIT'
    }
}
