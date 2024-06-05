import os
from flask import Flask, request, send_file

app = Flask(__name__)

DIR = "storage"


def cwd():
    """
    Returns directory containing this file
    """
    return os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def hello_world():
    return """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Form</title>
</head>
<body>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="file">Choose a file:</label>
        <input type="file" id="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "no file attached"
    file = request.files["file"]
    if file.filename == "":
        return "no file chosen"

    file.save(os.path.join(DIR, file.filename))
    return "file saved"


@app.route("/download/<filename>")
def download(filename):
    full_path = os.path.join(DIR, filename)
    if not os.path.exists(full_path):
        return "file not found", 404
    return send_file(full_path)
