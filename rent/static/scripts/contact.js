
  const form = document.getElementById("form"),
    email = document.getElementById("email"),
    name = document.getElementById("name"),
    message = document.getElementById("message")
  
    function submitClicked(el) {
      el.stopPropagation();
      el.preventDefault();
      if(validate()) {
        post('../message', getFormValue())
          .then(_ => {
            alert('Message sent.');
            formEl.reset();
          })
          .catch(err => 
           alert('Error')
          )
      } else {
      }
    }
  
    function post(url, body) {
    return fetch(url, {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'X-CSRFToken': csrf_token,
        'X-Requested-With': 'XMLHttpRequest'
      },
      body: JSON.stringify(body),
    })
    .then(response => response.json());
  }
  
  function validate() {
    return (email.value && 
            name.value && 
            message.value);
  }
  
  function getFormValue() {
    return {
      email: email.value,
      name: name.value,
      message: message.value,
      isReaded: 'False'
    }
  }
  
  form.onsubmit = submitClicked;
  