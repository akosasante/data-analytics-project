from app import app


@app.route("/")
def hello():
    return "hi"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
