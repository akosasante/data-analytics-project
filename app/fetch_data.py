from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_envvar('APP_CONFIG_PATH')
apikey_token = app.config['SPORTS_DATA_IO']
headers = {"Ocp-Apim-Subscription-Key": apikey_token}


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
def update_entity(entity):
    for e in entity:
        click.echo(f"updating {e}")
        # call update methods...
