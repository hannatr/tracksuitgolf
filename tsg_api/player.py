from tsg_api import config


def insert_players(client):
    players = [
        {"name": "Dan Hallimen", "current_handicap": 1},
        {"name": "Mike Riley", "current_handicap": 5.6},
        {"name": "Greg Short", "current_handicap": 7.7},
        {"name": "Brad Stratton", "current_handicap": 9.1},
        {"name": "Ricky Howcroft", "current_handicap": 10.5},
        {"name": "Brandon Stewart", "current_handicap": 10.8},
        {"name": "Jon Cummings", "current_handicap": 11.3},
        {"name": "Justin Chantra", "current_handicap": 11.6},
        {"name": "Mike Sturgis", "current_handicap": 14.2},
        {"name": "Tim Hanna", "current_handicap": 17.3},
        {"name": "Joel Wilson", "current_handicap": 20.8},
        {"name": "KOP", "current_handicap": 26},
    ]
    config.get_logger().info("Inserting players into database")
    for player in players:
        client.table("player").insert(player).execute()


def get_player_by_name(client, player_name, just_id=True):
    response = client.table("player").select("*").eq("name", player_name).execute()
    if response.data:
        if just_id:
            return response.data[0].get("id")
        else:
            return response.data[0]
    else:
        return None
