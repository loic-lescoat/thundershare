import os
from flask import Flask, request, send_file, \
        render_template, redirect, url_for
from collections import defaultdict

app = Flask(__name__)

DIR = os.environ['STORAGE_DIR']

messages=defaultdict(str)
messages['upload'] = "Uploaded file"
messages['delete'] = "Deleted file"
messages['No file attached'] = 'No file attached'
messages['No file chosen'] = 'No file chosen'


def cwd():
    """
    Returns directory containing this file
    """
    return os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def home():
    files = sorted(os.listdir(DIR))
    return render_template("home.html", files=files, message=messages[request.args.get('action')])


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(
                url_for(
                    'home',
                    action='No file attached'
                    )
                )
    file = request.files["file"]
    if file.filename == "":
        return redirect(
                url_for(
                    'home',
                    action='No file chosen'
                    )
                )

    file.save(os.path.join(DIR, file.filename))
    return redirect(
            url_for(
                'home',
                action='upload'
                )
            )


@app.route("/download/<filename>")
def download(filename):
    full_path = os.path.join(DIR, filename)
    if not os.path.exists(full_path):
        return "file not found", 404
    return send_file(full_path)

@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    full_path = os.path.join(DIR, filename)
    if not os.path.exists(full_path):
        return "file not found", 404
    os.remove(full_path)
    return redirect(
            url_for(
                'home',
                action='delete'
                )
            )
