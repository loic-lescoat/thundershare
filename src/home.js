
function my_alert(message, success){
  // TODO use success

  const alert_timeout = 3000;
  const notificationElement = document.getElementById('notification_message');

  notificationElement.textContent = message;
  notificationElement.style.visibility = 'visible';

setTimeout(() => {
        notificationElement.style.visibility = 'hidden';
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

