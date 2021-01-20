from flask import Flask
import base64
import requests

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')
apikey_token = app.config['SPORTS_DATA_IO']
headers = { "Ocp-Apim-Subscription-Key": apikey_token }


@app.route("/")
def hello():
    return "hi"

@app.route("/teams")
def all_active_teams():
    url = 'https://api.sportsdata.io/v3/nba/scores/json/teams'
    response = requests.get(url=url, headers=headers)
    print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    return response.content

@app.route("/players")
def all_active_players():
    url = 'https://api.sportsdata.io/v3/nba/scores/json/Players'
    response = requests.get(url=url, headers=headers)
    print('Response HTTP Status Code: {status_code}'.format(
        status_code=response.status_code))
    print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    return response.content

if __name__ == "__main__":
    app.run(host='0.0.0.0')
