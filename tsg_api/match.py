from tsg_api import config, player, scorecard, tournament


def populate_team_by_players(players):
    player_ids = []
    for p in players:
        player_ids.append(player.get_player_by_name(p))
    return player_ids


def insert_tobacco_road(client):
    config.get_logger().info("Inserting Tobacco Road matches into database")
    course_name = "Tobacco Road"
    t_id = tournament.get_tournament_by_name(client, "Tobacco Road Tournament")
    scoring_type = "best_ball_match_play"
    teams = [
        (["Jon Cummings", "KOP"], ["Mike Riley", "Joel Wilson"]),
        (["Brad Stratton", "Mike Sturgis"], ["Greg Short", "Justin Chantra"]),
        (["Dan Hallimen", "Brandon Stewart"], ["Ricky Howcroft", "Tim Hanna"]),
    ]
    for team in teams:
        match = {
            "tournament_id": t_id,
            "scoring_type": scoring_type,
            "team_1_scorecards": scorecard.get_sc_by_players_course(client, team[0], course_name),
            "team_2_scorecards": scorecard.get_sc_by_players_course(client, team[1], course_name),
        }
        client.table("match").insert(match).execute()


def insert_mid_pines(client):
    config.get_logger().info("Inserting Mid Pines matches into database")
    course_name = "Mid Pines"
    t_id = tournament.get_tournament_by_name(client, "Tobacco Road Tournament")
    scoring_type = "stableford"
    teams = [
        (["Brad Stratton", "KOP"], ["Justin Chantra", "Tim Hanna"]),
        (["Brandon Stewart", "Mike Sturgis"], ["Mike Riley", "Ricky Howcroft"]),
        (["Dan Hallimen", "Jon Cummings"], ["Greg Short", "Joel Wilson"]),
    ]
    for team in teams:
        match = {
            "tournament_id": t_id,
            "scoring_type": scoring_type,
            "team_1_scorecards": scorecard.get_sc_by_players_course(client, team[0], course_name),
            "team_2_scorecards": scorecard.get_sc_by_players_course(client, team[1], course_name),
        }
        client.table("match").insert(match).execute()


def insert_pine_needles(client):
    config.get_logger().info("Inserting Pine Needles matches into database")
    course_name = "Pine Needles"
    t_id = tournament.get_tournament_by_name(client, "Tobacco Road Tournament")
    scoring_type = "match_play"
    teams = [
        (["Dan Hallimen"], ["Mike Riley"]),
        (["Brad Stratton"], ["Greg Short"]),
        (["Brandon Stewart"], ["Ricky Howcroft"]),
        (["Jon Cummings"], ["Justin Chantra"]),
        (["Mike Sturgis"], ["Tim Hanna"]),
        (["KOP"], ["Joel Wilson"]),
    ]
    for team in teams:
        match = {
            "tournament_id": t_id,
            "scoring_type": scoring_type,
            "team_1_scorecards": scorecard.get_sc_by_players_course(client, team[0], course_name),
            "team_2_scorecards": scorecard.get_sc_by_players_course(client, team[1], course_name),
        }
        client.table("match").insert(match).execute()


def insert_matches(client):
    insert_tobacco_road(client)
    insert_mid_pines(client)
    insert_pine_needles(client)
