from flask import Flask
import base64
import requests

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')


@app.route("/")
def hello():
    return app.config['MY_SPORTSFEED_API_KEY']


if __name__ == "__main__":
    app.run(host='0.0.0.0')
