from kickbase import app
from kickbase.transfermarkt import liga, get_transfermarket, get_transfermarket_by_time
from kickbase.player import get_player_by_id
from kickbase.myteam import get_lineup_players
from kickbase.feed import liga, get_feed
from kickbase.mongodb.mongo_db_player import update_player

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/market')
def market():
    return get_transfermarket(liga)

@app.route('/market/filter')
def market_filter():
    return get_transfermarket_by_time(liga)




@app.route('/player/<player_id>')
def players(player_id):
    return get_player_by_id(player_id)


@app.route('/myteam')
def team():
    return get_lineup_players(liga)


@app.route('/feed')
def feed():
    return get_feed(0, liga)

@app.route('/refresh')
def refresh():
    return update_player()
