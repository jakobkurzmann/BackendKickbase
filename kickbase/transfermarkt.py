from kickbase_api.kickbase import Kickbase

from kickbase.constants import NUTZERNAME, PASSWORD

kickbase = Kickbase()
user, leagues = kickbase.login(NUTZERNAME, PASSWORD)

# This is my current league
liga = kickbase.leagues()[1]


def get_transfermarket(league_id):
    market = kickbase.market(league_id).players
    marketfeed = []
    for player in market:
        marketfeed.append(
            {
                "Spieler ID": player.id,
                "Vorname": player.first_name,
                "Nachname": player.last_name,
                "Average Points": player.average_points,
                "Total Points": player.totalPoints,
                "Marktwert": player.market_value,
                "Marktwert Trend": player.market_value_trend,
                "Position": player.position,
                "Status": player.status,
                "TeamID": player.team_id,
                "UserID": player.user_id,
                "Username": player.username,
                "User Path": player.user_profile_path,
                "Preis": player.price,
                "Abgelaufen": player.expiry,
            }
        )
    return marketfeed


def get_transfermarket_by_time(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Abgelaufen"], reverse=True)
    return transfermarket


def get_transfermarket_by_price(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Preis"])
    return transfermarket


def get_transfermarket_by_avg(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Average Points"])
    return transfermarket


def get_transfermarket_by_total(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Total Points"])
    return transfermarket


def get_transfermarket_by_trend(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Marktwert Trend"])
    return transfermarket


def get_transfermarket_by_position(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Position"])
    return transfermarket


def get_transfermarket_by_status(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["Status"])
    return transfermarket


def get_transfermarket_by_team(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["TeamID"])
    return transfermarket


def get_transfermarket_by_user(league_id):
    transfermarket = get_transfermarket(league_id)
    transfermarket.sort(key=lambda x: x["UserID"])
    return transfermarket


