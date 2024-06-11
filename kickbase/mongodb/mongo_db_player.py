from kickbase_api.kickbase import Kickbase
from kickbase import collection
from kickbase.constants import BUNDESLIGAIDS, NUTZERNAME, PASSWORD


kickbase = Kickbase()
kickbase.login(NUTZERNAME, PASSWORD)
liga = kickbase.leagues()[1]


def getPlayer():
    marketValueList = []

    for id in BUNDESLIGAIDS:
        team = kickbase.team_players(id)
        for player in team:
            dbPlayer = (player.id, player.first_name, player.last_name, player.team_id,
                        player.position, player.status,
                        player.average_points, player.totalPoints,
                        player.market_value,
                        player.market_value_trend,
                        player.profile_big_path,
                        )
            print(dbPlayer)
            marketValueList.append(dbPlayer)
    return marketValueList

def update_player():
    playerList = getPlayer()
    new = 0
    old = 0
    for player in playerList:
        if collection.find_one({'_id': str(player[0])}) is None:
            collection.insert_one({'_id': str(player[0]), 'firstname': player[1], 'lastname': player[2], 'teamID': player[3],
                                   'position': player[4], 'status': player[5], 'avgPoints': player[6], 'totalPoints': player[7],
                                   'marketValue': player[8], 'marketTrend': player[9], 'profilePictureBig': player[10]})
            new += 1
        else:
            collection.update_one({'_id': str(player[0])}, {'$set': {'marketValue': player[8], 'status': player[5],
                                                                    'marketTrend': player[9], 'avgPoints': player[6],
                                                                     'totalPoints': player[7]}})
            old += 1
    print('New: ' + str(new) + ' Old: ' + str(old))
    return 'New: ' + str(new) + ' Old: ' + str(old)

