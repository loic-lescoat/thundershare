
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
      update_list_of_files()
      my_alert(data, true)
    })
    .catch(error => {
      my_alert(error.message, false)
    })
  } else {
    my_alert("select a file", false)
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

function update_list_of_files(){
  // get stored files on backend
  fetch("/get_stored_files", {})
  .then(response => response.json())
  .then(
    data => {
      stored_files = document.getElementById("stored_files")
      console.log("data is", data)


      var list_items_html = data.map(function(file){
        console.log("file is", file)
        return `
              <li>
                  <form action="/delete/${file}" method="POST" class="flex space-x-2 items-center">
                      <button type="submit" formaction="/download/${file}" formmethod="GET" formtarget="_blank" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700">${file}</button>
                      <button type="submit" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-700">Delete</button>
                  </form>
              </li>
        `
      }).join("\n")

      stored_files.innerHTML = list_items_html

    }
  ) // don't bother catching
}

// main
update_list_of_files()
