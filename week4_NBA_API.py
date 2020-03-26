# https://pypi.org/project/nba-api/
from nba_api.stats.static import teams
import pandas as pd
import matplotlib.pyplot as plt


def one_dict(list_dict):
    keys = list_dict[0].keys()
    # print("one_dict, keys=", keys)
    out_dict = {key: [] for key in keys}
    # print("one_dict, out_dict=", out_dict)
    for dict_ in list_dict:
        # print("one_dict, dict_=", dict_)
        for key, value in dict_.items():
            # print("one_dict, 0) out_dict[key]=", key, value, out_dict[key])
            out_dict[key].append(value)
            # print("one_dict, 1) out_dict[key]=", key, value, out_dict[key])
    return out_dict


nba_teams = teams.get_teams()
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
print(df_teams.head())

#Will use the team's nickname to find the unique id, we can see the row that contains the warriors by using the column nickname as follows:
df_warriors=df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

#we can use the following line of code to access the first column of the dataframe:
id_warriors=df_warriors[['id']].values[0][0]
#we now have an integer that can be used   to request the Warriors information
print('id_warriors', id_warriors)

# The function "League Game Finder " will make an API call, its in the module stats.endpoints
from nba_api.stats.endpoints import leaguegamefinder
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
print(gamefinder)

#we can see the json file by running the following line of code.
print(gamefinder.get_json())

#The game finder object has a method get_data_frames(), that returns a dataframe.
# If we view the dataframe, we can see it contains information about all the games the Warriors played.
# The PLUS_MINUS column contains information on the score, if the value is negative the Warriors lost by that many points,
# if the value is positive, the warriors one by that amount of points.
# The column MATCHUP had the team the Warriors were playing, GSW stands for golden state and TOR means Toronto Raptors;
# vs signifies it was a home game and the @ symbol means an away game.
games = gamefinder.get_data_frames()[0]
print(games.head())

games_win = games[games['PLUS_MINUS'] > 0]
print(games_win.head())

games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

# We can calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away:
games_home.mean()['PLUS_MINUS']

#We can plot out the PLUS MINUS column for for the dataframes games_home and  games_away.
# We see the warriors played better at home.
fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()