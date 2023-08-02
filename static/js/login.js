let loginForm = document.getElementById('loginForm')

loginForm.addEventListener('submit' , async function(event){
    let postData = {
        'email' : event.target.username.value,
        'password' : event.target.password.value
    }
    let response = await fetch('/auth/token/' , {
        method : "POST",
        body :JSON.stringify(postData),
        headers :{
            'Content-Type' : 'application/json'
        }
        
    })
    let resData = await response.json()
    console.log(resData)
    if (!response.ok){
        alert(resData.detail)
    }
    else{
        localStorage.setItem('token' , resData.access)
    }

}) 