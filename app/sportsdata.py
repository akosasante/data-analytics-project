import requests
import json


class SportsdataAPI:
    """Pull data from https://sportsdata.io api"""

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, url):
        headers = { "Ocp-Apim-Subscription-Key": self.api_key }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception("ERROR")

    def get_all_teams(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/teams")

    def get_all_players(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Players")

    def get_all_stadiums(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Stadiums")

    def get_season_standings_for_year(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Standings/{season}".format(season=year))

    def get_all_star_players(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Standings/{season}".format(season=year))

    def get_games_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Games/{season}".format(season=year))

    def team_stats_allowed_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/stats/json/TeamStatsAllowedByPosition/{season}".format(season=year))

    def ingest_data(self, db, models):
        # Players
        all_players = models.SportsDataIO_NBAPlayer(raw_json=self.get_all_players())
        db.session.add(all_players)
        db.session.commit()

        # Teams
        all_teams = models.SportsDataIO_NBATeam(raw_json=self.get_all_teams())
        db.session.add(all_teams)
        db.session.commit()

        # Stadiums
        all_stadiums = models.SportsDataIO_NBAStadium(raw_json=self.get_all_stadiums())
        db.session.add(all_stadiums)
        db.session.commit()

