from flask import Flask
import base64
from sportsfeed import SportsdataAPI
import psycopg2


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')
apikey_token = app.config['SPORTS_DATA_IO']
headers = { "Ocp-Apim-Subscription-Key": apikey_token }


@app.route("/")
def hello():
    return "hi"

@app.route("/teams", methods=['POST'])
def insert_teams():
    sportsdata_api = SportsdataAPI(apikey_token)
    conn = psycopg2.connect(
        host="localhost",
        database="analytics",
        user="analytics",
        password="analytics"
    )
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
