from app import db, app
import click
import models
from sportsdata import SportsdataAPI

sportsdata_api_key = app.config['SPORTS_DATA_IO_API_KEY']


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    click.echo('initializing database')
    click.echo('dropping tables')
    db.drop_all()
    click.echo('recreating tables')
    db.create_all()


@cli.command()
def init_data():
    click.echo('ingest base data')
    click.echo('ingest nba data from sportsdata.io')
    ingest_sportsdata_data()


@cli.command()
@click.option('--year', '-y', default='', help='Which year\'s stats do you want to ingest?')
def get_year_data(year):
    click.echo('ingest season data')
    click.echo('ingest nba data from sportsdata.io')
    ingest_sportsdata_data_for_year(year)


@cli.command()
@click.option('--entity', '-e', default='', help='Which entity?')
def update_entity(entity):
    for e in entity:
        click.echo(f"updating {e}")
        # call update methods...


def ingest_sportsdata_data():
    SportsdataAPI(sportsdata_api_key).ingest_data(click, db, models)


def ingest_sportsdata_data_for_year(year):
    SportsdataAPI(sportsdata_api_key).ingest_season_data(year, click, db, models)


if __name__ == '__main__':
    cli()
