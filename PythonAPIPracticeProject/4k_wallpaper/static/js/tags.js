(function Program() {
    "use strict";

    if (window.tagsArr === undefined || window.tagsArr === null || !window.tagsArr) {
        window.tagsArr = []
    }
    renderTags();

    document.querySelector("#addButton").addEventListener("click", function(event){
        event.preventDefault()

        let tagString = document.querySelector("#tagInput").value.trim()

        if(tagString!== null && tagString !== '' && !tagString.includes(',')){
            window.tagsArr.push(tagString)
            renderTags();
        }

        document.querySelector("#tagInput").value = ''
    });
}());


function submitTags() {
    document.getElementById("tagInput").value = window.tagsArr.join(',')
    document.getElementById("finalForm").submit()
    document.getElementById("tagInput").value = ''
}

function renderTags() {
    document.querySelector('#tagsContainer').innerHTML = ''
    let i = 1
    for (const tagString of window.tagsArr) {
        document.querySelector('#tagsContainer').innerHTML += `<span class="badge rounded-pill text-bg-primary" id="tag${i}" onclick="removeTag('${tagString}')"> <span>${tagString}</span> <button class="btn p-0 ms-1">x</button></span>`
        i += 1
    }
}

function removeTag(element) {
    const index = window.tagsArr.indexOf(element);
    
    if (index !== -1) {
        window.tagsArr.splice(index, 1);
        renderTags();
    }

}
