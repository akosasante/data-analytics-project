from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')
db = SQLAlchemy(app)
