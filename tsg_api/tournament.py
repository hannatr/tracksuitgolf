from tsg_api import config, player


def insert_tournament(client):
    team_1 = []
    team_2 = []
    for p in ["Dan Hallimen", "Brad Stratton", "Brandon Stewart", "Jon Cummings", "Mike Sturgis", "KOP"]:
        team_1.append(player.get_player_by_name(client, p))

    for p in ["Mike Riley", "Greg Short", "Ricky Howcroft", "Justin Chantra", "Tim Hanna", "Joel Wilson"]:
        team_2.append(player.get_player_by_name(client, p))

    tournament = {
        "name": "Tobacco Road Tournament",
        "year": 2024,
        "team_1": team_1,
        "team_2": team_2,
    }

    config.get_logger().info("Inserting tournament into database")
    client.table("tournament").insert(tournament).execute()


def get_tournament_by_name(client, tournament_name):
    response = client.table("tournament").select("*").eq("name", tournament_name).execute()
    if response.data:
        return response.data[0].get("id")
    else:
        return None
