from flask import Flask, render_template, request

app = Flask(__name__)


# GETの時のルーティング
@app.route("/", methods=["GET"])
# @app.get("/")  # これでもOK
def index_get():
    return render_template("index.html")


# POSTの時のルーティング
@app.route("/", methods=["POST"])
# @app.post("/")  # これでもOK
def index_post():
    message = request.form["message"]
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
