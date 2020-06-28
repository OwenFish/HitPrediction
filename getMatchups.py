from datetime import date
import statsapi

date = "07/25/2019"#date.today().strftime("%m%d%y")

#params = {'date': today.strftime('%m/%d%y')}
Schedparams = {'date':date, \
    'sportId':1,\
    'hydrate':'probablePitcher(note)',\
    'fields':'dates,date,games,gamePk,gameDate,status,abstractGameState,teams,away,home,team,id,name,probablePitcher,id,fullName'}


today = statsapi.get('schedule',Schedparams)

for day in today['dates']:
    print('{}'.format(day['date']))
    for game in day['games']:
        homeTeam = game['teams']['home']['team']['name']
        homeID = game['teams']['home']['team']['id']
        homePitcher = game['teams']['home']['probablePitcher']['fullName']
        homePitcherID = game['teams']['home']['probablePitcher']['id']
        homeParams = rosterParams = {"rosterType": 'active', "season": date.split('/')[-1], "teamId": homeID, "date": date}
        homeRoster = statsapi.get("team_roster", homeParams)

        awayTeam = game['teams']['away']['team']['name']
        awayID = game['teams']['away']['team']['id']
        awayPitcher = game['teams']['away']['probablePitcher']['fullName']
        awayPitcherID = game['teams']['away']['probablePitcher']['id']
        awayParams = {"rosterType": 'active', "season": date.split('/')[-1], "teamId": awayID, "date": date}
        awayRoster = statsapi.get("team_roster", awayParams)

        for plr in awayRoster['roster']:
            if plr['position']['abbreviation'] != 'P':
                print(f"{plr['person']['fullName']},{homePitcher}")

        for plr in homeRoster['roster']:
            if plr['position']['abbreviation'] != 'P':
                print(f"{plr['person']['fullName']},{awayPitcher}")
