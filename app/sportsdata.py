import requests
import json


class SportsdataAPI:
    """Pull data from https://sportsdata.io api. See data types described in
    https://sportsdata.io/developers/data-dictionary/nba """

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, url):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception("ERROR")

    # data type = [Team]
    def get_all_teams(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/AllTeams")

    # data type = [Player]
    def get_all_players(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Players")

    # data type = [Stadium]
    def get_all_stadiums(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Stadiums")

    # data type = [Standings]
    def get_season_standings_for_year(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Standings/{season}".format(season=year))

    # data type = [PlayerInfo]
    def get_all_star_players(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/stats/json/AllStars/{season}".format(season=year))

    # data type = [Game]
    def get_games_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Games/{season}".format(season=year))

    # data type = [Team Season]
    def get_team_stats_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/TeamSeasonStats/{season}".format(season=year))

    # data type = [Player Season]
    def get_player_stats_for_season(self, year):
        return self.request(
            " https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/{season}".format(season=year))

    def ingest_data(self, click, db, models):
        # Players
        click.echo("fetching/inserting players")
        all_players = models.SportsDataIO_NBAPlayer(raw_json=self.get_all_players())
        db.session.add(all_players)
        db.session.commit()

        # Teams
        click.echo("fetching/inserting teams")
        all_teams = models.SportsDataIO_NBATeam(raw_json=self.get_all_teams())
        db.session.add(all_teams)
        db.session.commit()

        # Stadiums
        click.echo("fetching/inserting stadiums")
        all_stadiums = models.SportsDataIO_NBAStadium(raw_json=self.get_all_stadiums())
        db.session.add(all_stadiums)
        db.session.commit()

    def ingest_season_data(self, year, click, db, models):
        # Standings
        click.echo("fetching standings for {year}".format(year=year))
        standings = models.SportsDataIO_NBASeasonStandings(raw_json=self.get_season_standings_for_year(year), year=year)
        db.session.add(standings)

        # All-Stars
        click.echo("fetching all-stars for {year}".format(year=year))
        all_stars = models.SportsDataIO_NBASeasonAllStars(raw_json=self.get_all_star_players(year), year=year)
        db.session.add(all_stars)

        # Game Stats
        click.echo("fetching game stats for {year}".format(year=year))
        games = models.SportsDataIO_NBASeasonGameStats(raw_json=self.get_games_for_season(year), year=year)
        db.session.add(games)

        # Team Season Stats
        click.echo("fetching team stats for {year}".format(year=year))
        teams = models.SportsDataIO_NBASeasonTeamStats(raw_json=self.get_team_stats_for_season(year), year=year)
        db.session.add(teams)

        # Player Season Stats
        click.echo("fetching players for {year}".format(year=year))
        teams = models.SportsDataIO_NBASeasonPlayerStats(raw_json=self.get_player_stats_for_season(year), year=year)
        db.session.add(teams)

        click.echo("committing data")
        db.session.commit()
