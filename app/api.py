from flask import Flask
import base64
import requests
from flask_sqlalchemy import SQLAlchemy
import click, datetime
from sqlalchemy.dialects.postgresql import JSONB

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')
apikey_token = app.config['SPORTS_DATA_IO']
headers = { "Ocp-Apim-Subscription-Key": apikey_token }
db = SQLAlchemy(app)

from app import models

@click.command()
def init_db():
    click.echo('init_db')
    meta = db.metadata
    db.drop_all()
    # for table in reversed(meta.sorted_tables):
    #     print ('Clear table %s' % table)
    #     table.delete()
    #     db.session.commit()
    db.create_all()

@click.command()
def init_data():
    click.echo('ingest base data')
    click.echo('ingest nba players from sportsdata.io')
    # call your ingestion methods.

@click.command()
@click.option('--entity', '-e', default='', help='Which entity?')
def update_entity():
    for e in entity:
        click.echo(f"updating {e}")
        # call update methods... 


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
    app.run(host='0.0.0.0', debug=True)
