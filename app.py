import os
from flask import (
    Flask,
    request,
    send_from_directory,
    send_file,
    render_template,
    redirect,
    url_for,
)
from collections import defaultdict
from typing import List
import json

app = Flask(__name__)

TEXT_STORE = "TEXT_STORE"

DIR = os.environ["STORAGE_DIR"]


def cwd():
    """
    Returns directory containing this file
    """
    return os.path.dirname(os.path.realpath(__file__))


def _get_stored_files() -> List[str]:
    files = sorted((x for x in os.listdir(DIR) if x != TEXT_STORE))
    return files


@app.route("/")
def home():
    if os.path.exists(os.path.join(DIR, TEXT_STORE)):
        with open(os.path.join(DIR, TEXT_STORE)) as f:
            user_text = f.read()
    else:
        user_text = ""
    return render_template(
        "home.html",
        user_text=user_text,
    )


@app.route("/favicon.ico")
def favicon():
    return send_file("./favicon.ico")


@app.route("/src/<path:filename>")
def serve_src(filename: str):
    directory = os.path.join(app.root_path, "src")

    if os.path.isfile(os.path.join(directory, filename)):
        return send_from_directory(directory, filename)
    else:
        return "file not found", 404


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file attached"
    file = request.files["file"]
    if file.filename == "":
        return "No file chosen"

    file.save(os.path.join(DIR, file.filename))
    return "File uploaded successfully"


@app.route("/upload_text", methods=["POST"])
def upload_text():
    new_text = request.form.get("text")

    with open(os.path.join(DIR, TEXT_STORE), "w") as f:
        f.write(new_text)

    return "Text updated successfully"


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
        return "File not found", 404
    os.remove(full_path)
    return "File deleted"


@app.route("/get_stored_files")
def get_stored_files():
    files = _get_stored_files()
    return json.dumps(files)
