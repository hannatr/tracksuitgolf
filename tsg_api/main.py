from supabase import Client, create_client

from tsg_api import config, course, match, player, scorecard, tournament

if __name__ == "__main__":
    logger = config.load_configuration()
    supabase: Client = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)

    # Test connection with client
    response = supabase.table("player").select("*").limit(1).execute()
    logger.info(f"Successfully connected to Supabase app at {config.SUPABASE_URL}")

    player.insert_players(supabase)
    course.insert_courses(supabase)
    tournament.insert_tournament(supabase)
    scorecard.insert_scorecards(supabase)
    match.insert_matches(supabase)
