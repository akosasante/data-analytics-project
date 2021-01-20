import requests


class SportsdataAPI:
    """Pull data from https://sportsdata.io api"""
    
    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, url):
        headers = { "Ocp-Apim-Subscription-Key": self.api_key }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception("ERROR")

    def get_all_teams(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/teams")

    def get_all_players(self):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Players")
    
    def get_season_standings_for_year(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Standings/{season}".format(season=year))

    def get_all_star_players(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Standings/{season}".format(season=year))

    def get_games_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/scores/json/Games/{season}".format(season=year))

    def team_stats_allowed_for_season(self, year):
        return self.request("https://api.sportsdata.io/v3/nba/stats/json/TeamStatsAllowedByPosition/{season}".format(season=year))