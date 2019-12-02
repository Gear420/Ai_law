from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import send_file
import os

#给flask引入下载文件能力.

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/api/download/<path:filename>")
def download(filename):
    dirpath = os.path.join(app.root_path, 'genDocx')
    print(dirpath)
    return send_from_directory(dirpath, filename, as_attachment=True)
    # as_attachment=True 一定要写，不然会变成打开，而不是下载
@app.route("/api/upload",methods=["GET","POST"])
def upload():



