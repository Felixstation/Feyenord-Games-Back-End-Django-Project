let grid = document.querySelector(".product-wrapper-grid")
let filterInput = document.getElementById("filterInput")

fetch('/api/products')
    .then(res=> res.json())
    .then(json => {

        for (let value of json){

            addElement(grid , value)
        }

    })


filterInput.addEventListener('onclick' , filterProducts);

function filterProducts(){

    let filterValue = filterInput.value.toUpperCase();
    let item = grid.querySelectorAll('.row')

    for (let i = 0; i< item.length; i++){

        let span = item[i].querySelector('.title');

        if(span.innerHTML.toUpperCase().indexOf(filterValue) > -1){
            item[i].style.display = "initial"
        }else{
            item[i].style.display = "none"
        }

    }

    

}



function addElement(appenln , value){
    let div = document.createElement('div')
    div.className = "row margin-res"

    let{thumbnail , product_id , category , price} = value

    div.innerHTML = `
    <div class="col-xl-3 col-6 col-grid-box">
    <div class="product-box">
        <div class="img-wrapper">
            <div class="front">
                <a href=""><img src="${thumbnail}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
            </div>
            <div class="back">
                <a href=""><img src="${thumbnail}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
            </div>
            <div class="cart-info cart-wrap">
                <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                        class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                        class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                        class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                        class="ti-reload" aria-hidden="true"></i></a>
            </div>
        </div>
        <div class="product-detail">
            <div>
                <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
                <a href=>
                    <h6 class="title">${product_id.name}</h6>
                </a>
                <p>
                </p>
                <h4 >$ ${price}</h4>
                <ul class="color-variant">
                    <li class="bg-light0"></li>
                    <li class="bg-light1"></li>
                    <li class="bg-light2"></li>
                </ul>
            </div>
        </div>
    </div>
  </div>
    
    `

    appenln.appendChild(div);

}





