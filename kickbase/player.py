from kickbase_api.kickbase import Kickbase
from kickbase import collection
from kickbase.constants import BUNDESLIGAIDS, NUTZERNAME, PASSWORD


kickbase = Kickbase()
kickbase.login(NUTZERNAME, PASSWORD)
liga = kickbase.leagues()[1]


# Funktion sucht einen Spieler anhand der ID in der Datenbank(MongoDB) und gibt die Daten zurück
def get_player_by_id(player_id):
    player = collection.find_one({'_id': str(player_id)})
    return player
