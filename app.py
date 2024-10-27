import os
from flask import (
    Flask,
    Blueprint,
    request,
    send_file,
    render_template,
    render_template_string,
    make_response,
)
from typing import List
import json
from constants import URL_REGEX
import re

app = Flask(__name__)

TEXT_STORE = "TEXT_STORE"

DIR = os.environ["STORAGE_DIR"]

bp = Blueprint("thundershare", __name__, url_prefix="/thundershare")


def cwd():
    """
    Returns directory containing this file
    """
    return os.path.dirname(os.path.realpath(__file__))


def _get_stored_files() -> List[str]:
    files = sorted((x for x in os.listdir(DIR) if x != TEXT_STORE))
    return files


@bp.route("/")
def home():
    if os.path.exists(os.path.join(DIR, TEXT_STORE)):
        with open(os.path.join(DIR, TEXT_STORE)) as f:
            user_text = f.read()
    else:
        user_text = ""

    links = re.findall(URL_REGEX, user_text)
    return render_template(
        "home.html",
        user_text=user_text,
        links=links,
    )


@bp.route("/favicon.ico")
def favicon():
    return send_file("./favicon.ico")


@bp.route("/src/<path:filename>")
def serve_src(filename: str):
    directory = os.path.join(app.root_path, "src")

    full_path = os.path.join(directory, filename)
    if os.path.isfile(full_path):
        # ignore race condition
        with open(full_path, "r") as f:
            contents = f.read()
        content = render_template_string(contents, x="hi from here!!!")
        response = make_response(content)
        response.mimetype = "application/javascript"
        return response

    else:
        return "file not found", 404


@bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file attached"
    file = request.files["file"]
    if file.filename == "":
        return "No file chosen"

    file.save(os.path.join(DIR, file.filename))
    return "File uploaded successfully"


@bp.route("/upload_text", methods=["POST"])
def upload_text():
    new_text = request.form.get("text")

    with open(os.path.join(DIR, TEXT_STORE), "w") as f:
        f.write(new_text)

    return "Text updated successfully"


@bp.route("/download/<filename>")
def download(filename):
    full_path = os.path.join(DIR, filename)
    if not os.path.exists(full_path):
        return "file not found", 404
    return send_file(full_path)


@bp.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    full_path = os.path.join(DIR, filename)
    if not os.path.exists(full_path):
        return "File not found", 404
    os.remove(full_path)
    return "File deleted"


@bp.route("/get_stored_files")
def get_stored_files():
    files = _get_stored_files()
    return json.dumps(files)


app.register_blueprint(bp)
