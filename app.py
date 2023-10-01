from flask import Flask, url_for, render_template, request
from Digits_model import main

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        image = request.form["output"]
        preds = main(image)
        return render_template("index.html", preds=preds)
    return render_template("index.html", preds="")


if __name__ == "__main__":
    app.run(debug=True)
