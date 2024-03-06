from tsg_api import config, course, player


def insert_scorecards(client):
    players = [
        "Dan Hallimen",
        "Mike Riley",
        "Greg Short",
        "Brad Stratton",
        "Ricky Howcroft",
        "Brandon Stewart",
        "Jon Cummings",
        "Justin Chantra",
        "Mike Sturgis",
        "Tim Hanna",
        "Joel Wilson",
        "KOP",
    ]
    courses = [("Tobacco Road", "2024/03/18"), ("Mid Pines", "2024/03/19"), ("Pine Needles", "2024/03/20")]

    config.get_logger().info("Inserting scorecards into database")
    for p in players:
        p_data = player.get_player_by_name(client, p, just_id=False)
        for c, date in courses:
            c_id = course.get_course_by_name(client, c)
            scorecard = {
                "player_id": p_data.get("id"),
                "course_id": c_id,
                "date_played": date,
                "playing_hcp": p_data.get("current_handicap"),
                "strokes": [0] * 18,
            }
            client.table("scorecard").insert(scorecard).execute()


def get_sc_by_player_course(client, player_id, course_id):
    response = client.table("scorecard").select("*").eq("player_id", player_id).eq("course_id", course_id).execute()
    if response.data:
        return response.data[0].get("id")
    else:
        return None


def get_sc_by_players_course(client, players, course_name):
    scorecards = []
    c_id = course.get_course_by_name(client, course_name)
    for p in players:
        p_id = player.get_player_by_name(client, p)
        scorecards.append(get_sc_by_player_course(client, p_id, c_id))
    return scorecards
