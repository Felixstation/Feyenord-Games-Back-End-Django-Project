let reviewForm = document.getElementById('review-form')
reviewForm.addEventListener('submit' , function(e){
    e.preventDefault()
    let productElement = document.getElementById('review-content')
    let productId = productElement.getAttribute('data-product-id')
    let user = productElement.getAttribute('user')
    console.log(user)
    let content = document.getElementById('review-content')


    fetch(`/api/products/${productId}/comments/create/` , {
        method: 'POST',
        headers:{
            'Content-Type' : 'application/json',
            'X-CSRFToken' : reviewForm.csrfmiddlewaretoken.value
        },

        

        body: JSON.stringify(
        {'content' : content.value , 'product_version' : productId , 'user' : user},
        )
    })


    
})




const fetchComments = (productId) => {
    console.log(productId)
    return fetch(`/api/products/${productId}/comments/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .catch((error) => {
        console.error('Error fetching comments:', error);
        return [];
      });
  };
  
  // Function to display comments in the HTML
  const displayComments = (comments) => {
    const commentList = document.getElementById('commentList');
  
    // Clear existing comments
    commentList.innerHTML = '';
  
    // Add each comment to the list
    comments.forEach((comment) => {
      const listItem = document.createElement('li');
      listItem.innerHTML = `
      <ul class="comment-list">
                <li class="comment">
                    <div class="vcard bio">
                        <img height="85px" width="85px"
                            src="${comment.user.imageURL}"
                            alt="Image placeholder">

                    </div>
                    <div class="comment-body">
                        <h3>${comment.user.first_name} ${comment.user.last_name}</h3>
                        <h4>${comment.content}</h4>
                        <p><a href="#" class="reply">Reply</a></p>
                     </div>
                 </li>
       </ul>
      `;
      commentList.appendChild(listItem);
    });
  };
  
  // Get the product ID (replace '1' with the actual ID)
  const productElement = document.getElementById('commentList');
  const productId = productElement.getAttribute('data-product-id')
  
  // Fetch comments and display them
  fetchComments(productId)
    .then((data) => displayComments(data))
    .catch((error) => console.error('Error:', error));



function addComment() {
      // Get the value of the new comment from the input field
  const newCommentText = document.getElementById('review-content').value.trim();
  const newComment = document.getElementById('review-content')
  const demoUser = document.getElementById('demo-review')
  let user = demoUser.getAttribute('user')
  let image = newComment.getAttribute('image')
  let created_at = newComment.getAttribute('created-at')
  
      // Check if the comment is not empty
  if (newCommentText !== '') {
          // Create a new list item to represent the comment
    const newCommentItem = document.createElement('li');
    newCommentItem.innerHTML= `
    <div class="alert alert-success" role="alert">
        Review Was Sent!
    </div>
    <ul class="comment-list">
    <li class="comment">
        <div class="vcard bio">
            <img height="85px" width="85px"
                src="${image}"
                alt="Image placeholder">

        </div>
        <div class="comment-body">
            <h3>${user}</h3>
            <h4>${newCommentText}</h4>
            <p><a href="#" class="reply">Reply</a></p>
         </div>
     </li>
</ul>
    
    `
  
    // Append the new comment to the list
    const commentList = document.getElementById('commentList');
    commentList.appendChild(newCommentItem);
  

      }
  }


    
