function E(selector, parent) {
    if (selector instanceof HTMLElement) 
        return selector;
        
    return (parent || document).querySelectorAll(selector);
}

function hasClass(element, className) {
    return element.classList.contains(className);
}

function radioClass(element, className) {
    E("." + className).forEach((elem)=> 
    elem.classList.remove(className));
    element.classList.toggle(className);
}

function tabs(nav) {
    let navElem = E(nav)[0];

    navElem.addEventListener("click", (e) => {
        let target = e.target;

        if(hasClass(target, "tab"))
            radioClass(target, "active");
        
        let linkedTab = E("." + target.id)[0];

        radioClass(linkedTab, "visible");


    });

    let active = E(".tab.active")[0];
    if (active) {
            radioClass(E("."+active.id)[0], "visible");
    }

}

tabs(".menu-nav")



let loadMoreBtn1 = document.querySelector('#load-more-1');
let currentItem1 = 4;

loadMoreBtn1.onclick = () => {
    let boxes = [...document.querySelectorAll('.box-container-1 .box-1')];
    for(var i = currentItem1; i < currentItem1 + 4; i++) {
        boxes[i].style.display = 'inline-block';
    }
    currentItem1 += 4;
    if(currentItem1 >= boxes.length) {
        loadMoreBtn1.style.display = 'none'
    }
}


let loadMoreBtn2 = document.querySelector('#load-more-2');
let currentItem2 = 4;

loadMoreBtn2.onclick = () => {
    let boxes = [...document.querySelectorAll('.box-container-2 .box-2')];
    for(var i = currentItem2; i < currentItem2 + 4; i++) {
        boxes[i].style.display = 'inline-block';
    }
    currentItem2 += 4;
    if(currentItem2 >= boxes.length) {
        loadMoreBtn2.style.display = 'none'
    }
}

let loadMoreBtn3 = document.querySelector('#load-more-3');
let currentItem3 = 4;

loadMoreBtn3.onclick = () => {
    let boxes = [...document.querySelectorAll('.box-container-3 .box-3')];
    for(var i = currentItem3; i < currentItem3 + 4; i++) {
        boxes[i].style.display = 'inline-block';
    }
    currentItem3 += 4;
    if(currentItem3 >= boxes.length) {
        loadMoreBtn3.style.display = 'none'
    }
}


// ESTO ES LO NUEVO DEL 2/10/2023

// Obtén referencias a los elementos HTML
var abrirModal = document.getElementById("abrirModal");
var cerrarModal = document.getElementById("cerrarModal");
var miModal = document.getElementById("miModal");

// Abre el modal al hacer clic en el icono del carrito
abrirModal.addEventListener("click", function() {
    miModal.style.display = "block";
});

// Cierra el modal al hacer clic en el botón de cerrar
cerrarModal.addEventListener("click", function() {
    miModal.style.display = "none";
});

// Cierra el modal si el usuario hace clic fuera de él
window.addEventListener("click", function(event) {
    if (event.target == miModal) {
        miModal.style.display = "none";
    }
});
