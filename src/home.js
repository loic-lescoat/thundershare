
function toggle_all(element, classes_to_toggle){
  for (let key in classes_to_toggle){
    element.classList.toggle(classes_to_toggle[key])
  }
}

function my_alert(message, success){
  // TODO use success

  const alert_timeout = 2000;
  const notificationElement = document.getElementById('notification_message');

  notificationElement.textContent = message;
  notificationElement.style.visibility = 'visible'

  var new_style
  if (success){
    new_style = "bg-blue-100 border-t border-b border-blue-500 text-blue-700 px-4 py-3"
  } else {
    new_style = "bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
  }
  new_style = new_style.split(" ")

  console.log(new_style)

  toggle_all(notificationElement, new_style)


setTimeout(() => {
        notificationElement.style.visibility = 'hidden';
        toggle_all(notificationElement, new_style)
    },
    alert_timeout);
}

document.getElementById('upload_file').addEventListener('click', function() {
  const file_input = document.getElementById("file")
  const file = file_input.files[0]

  if (file){
    const form_data = new FormData()
    form_data.append("file", file)

    fetch("/upload", {
      method: 'POST',
      body: form_data
    })
    .then(response => response.text())
    .then(data => {
      my_alert(data, true)
    })
    .catch(error => {
      my_alert(error.message, false)
    })
  } else {
    alert("select a file")
  }
})

document.getElementById('upload_text').addEventListener('click', function() {
  const file_input = document.getElementById("text_input").value
  data = new URLSearchParams()
  data.append("text", file_input)

  fetch("/upload_text", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: data.toString(),
  })
  .then(response => response.text())
  .then(data => {
    my_alert(data, true)
  }).catch(error => {
    my_alert(error.message, false)
  })

})


