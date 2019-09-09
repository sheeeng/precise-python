from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello, World!</h3>" \
        + "<p/>" \
        + "<pre>" \
        + "UTC  : <b>" \
        + datetime.utcnow().isoformat(sep='T', timespec='auto') \
        + "</b>" \
        + "</pre>" \
        + "<pre>" \
        + "Local: <b>" \
        + datetime.now().isoformat(sep='T', timespec='auto') \
        + "</b>" \
        + "</pre>"
    return html


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=80
    )
