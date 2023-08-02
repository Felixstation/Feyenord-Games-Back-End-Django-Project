const ProductSearch= async (name)=>{
    console.log(name);
    let search = this.document.querySelector('#searchbar')
    search.innerHTML=""
    let response = await fetch(`/api/products?search=${name}`
        )
    let resData = await response.json()
   
    console.log(resData);
    

    for (value of resData){
        let storage=""
       if (value.storage_id){
           storage = value.storage_id.name
       }
       else{
           storage=""
       }
       ;

    

    
         let color=""
        if (value.color_id){
            color = value.color_id.name
        }
        else{
            color=""
        }
        ;
    
    console.log(value.get_images)

    search.innerHTML += `
    <div class="col-xl-2 col-md-4 col-sm-6">
        <div class="product-box">
            <div class="img-wrapper">
            <div class="front">
            <a href= "${value.get_absolute_url}"><img
                    src= ${value.thumbnail}
                    class="img-fluid blur-up lazyload bg-img" alt=""></a>
                </div>
                <div class="back">
            <a href="${value.get_absolute_url}"><img
                    src=${value.thumbnail}
                    class="img-fluid blur-up lazyload bg-img" alt=""></a>
        </div>
        <div class="cart-info cart-wrap">
            <button data-toggle="modal" data-target="#addtocart"
                title="Add to cart"><i class="ti-shopping-cart"></i></button> <a
                href="javascript:void(0)" title="Add to Wishlist"><i
                    class="ti-heart" aria-hidden="true"></i></a> <a href="#"
                data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                    class="ti-search" aria-hidden="true"></i></a> <a
                href="compare.html" title="Compare"><i class="ti-reload"
                aria-hidden="true"></i></a></div>
        </div>
            <div class="product-detail">
                <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i
                    class="fa fa-star"></i> <i class="fa fa-star"></i> <i
                    class="fa fa-star"></i></div>
                    <a href="{% url 'product:productpage'  i.slug %}">
                    <h6>$ ${value.price}</h6></a>
                    <h4>${value.product_id.name} </h4>
            </div>            
        
        <ul class="color-variant"> 
            <li class="bg-light1"></li>
            <li class="bg-light2"></li>
        </ul>
        </div>
    </div>
    </div>

`
}}

window.addEventListener('load', async  function(event){
    // let response = await fetch ('http://localhost:8000/api/products?search={}')
    // let resData = await response.json()
    // let search = this.document.querySelector('#searchbar')
    const urlParams= new URLSearchParams(window.location.search)
     const param=urlParams.get("search")
     ProductSearch(param)

})

let SearchForm = this.document.querySelector('#SearchForm')

SearchForm.addEventListener('submit' , function(event){
    event.preventDefault()
    
    let search = event.target.search.value
    // const urlParams= new URLSearchParams(window.location.search)
    //  urlParams.set("search",search)
    // window.location.search=urlParams.toString()
    var url= new URL(window.location.href)
    url.searchParams.set("search",search)
    // url.searchParams.append("search",search)
    window.history.pushState(null,null,url)
    // window.history.replaceState({},
    //     "search",
    //     replaceQueryString(location.href , "search", search))

    ProductSearch(search)
})





// let SearchForm2 = this.document.querySelector('#SearchForm2')

// SearchForm2.addEventListener('submit' , function(event){
//     // event.preventDefault()
//     let search = event.target.search.value
//     ProductSearch2(search)
// })
// const ProductSearch2= async (name)=>{

//     let response = await fetch (`http://localhost:8000/api/products?search=${name}`)
//     let resData = await response.json()
//     let search = this.document.querySelector('#searchbar2')
//     search.innerHTML=""

//     for (value of resData){
//         let storage=""
//        if (value.storage_id){
//            storage = value.storage_id.name
//        }
//        else{
//            storage=""
//        }
//        ;



//          let color=""
//         if (value.color_id){
//             color = value.color_id.name
//         }
//         else{
//             color=""
//         }
//         ;

//     search.innerHTML += `
//     <div class="col-xl-2 col-md-4 col-sm-6">
// <div class="product-box">
//     <div class="img-wrapper">
//         <div class="front">
//             <a href=""><img
//                     src=""
//                     class="img-fluid blur-up lazyload bg-img" alt=""></a>
//                 </div>
//                 <div class="back">
//             <a href=""><img
//                     src=""
//                     class="img-fluid blur-up lazyload bg-img" alt=""></a>
//         </div>
//         <div class="cart-info cart-wrap">
//             <button data-toggle="modal" data-target="#addtocart"
//                 title="Add to cart"><i class="ti-shopping-cart"></i></button> <a
//                 href="javascript:void(0)" title="Add to Wishlist"><i
//                     class="ti-heart" aria-hidden="true"></i></a> <a href="#"
//                 data-toggle="modal" data-target="#quick-view" title="Quick View"><i
//                     class="ti-search" aria-hidden="true"></i></a> <a
//                 href="compare.html" title="Compare"><i class="ti-reload"
//                 aria-hidden="true"></i></a></div>
//             </div>
//             <div class="product-detail">
//                 <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i
//                     class="fa fa-star"></i> <i class="fa fa-star"></i> <i
//                     class="fa fa-star"></i></div>
//                     <a href="{% url 'product:productpage'  i.slug %}">
                        
//                         <h6>$ ${value.price}</h6>
//         </a>
        
//         <h4>${value.product_id.name} ${color}</h4>
//         <ul class="color-variant"> 
//             <li class="bg-light1"></li>
//             <li class="bg-light2"></li>
//         </ul>
//     </div>
// </div>        
// </div>
// `
// }}}