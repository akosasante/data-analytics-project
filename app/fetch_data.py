from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_PATH')
db = SQLAlchemy(app)
# apikey_token = app.config['SPORTS_DATA_IO_API_KEY']
# headers = {"Ocp-Apim-Subscription-Key": apikey_token}

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    click.echo('init_db')
    meta = db.metadata
    db.drop_all()
    # for table in reversed(meta.sorted_tables):
    #     print ('Clear table %s' % table)
    #     table.delete()
    #     db.session.commit()
    db.create_all()


@cli.command()
def init_data():
    click.echo('ingest base data')
    click.echo('ingest nba players from sportsdata.io')
    # call your ingestion methods.


@cli.command()
@click.option('--entity', '-e', default='', help='Which entity?')
def update_entity(entity):
    for e in entity:
        click.echo(f"updating {e}")
        # call update methods...


if __name__ == '__main__':
    cli()
