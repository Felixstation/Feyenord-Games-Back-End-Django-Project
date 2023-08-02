let subscribeForm = document.getElementById('subscribe-form')
subscribeForm.addEventListener('submit' , function(e){
    e.preventDefault()
    let email = document.getElementById('subscribe-email')
    fetch('/api/subscribers/' , {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': subscribeForm.csrfmiddlewaretoken.value
        },

        body:JSON.stringify({'email': email.value})
    })

    .then(response => {

        if(response.ok){
            subscribeForm.innerHTML = 'Thanks for Subscribing!'
        }

        else{
            alert('Please Check Your Information!')
        }

    })

})
