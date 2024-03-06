from tsg_api import config


def insert_courses(client):
    courses = [
        {
            "name": "Tobacco Road",
            "pars": [5, 4, 3, 5, 4, 3, 4, 3, 4, 4, 5, 4, 5, 3, 4, 4, 3, 4],
            "handicaps": [3, 11, 17, 9, 15, 13, 7, 5, 1, 6, 10, 14, 2, 8, 12, 16, 18, 4],
        },
        {
            "name": "Mid Pines",
            "pars": [4, 3, 4, 4, 5, 5, 4, 3, 4, 5, 3, 4, 3, 4, 5, 4, 4, 4],
            "handicaps": [5, 15, 7, 13, 9, 1, 3, 17, 11, 2, 18, 8, 10, 16, 12, 6, 14, 4],
        },
        {
            "name": "Pine Needles",
            "pars": [5, 4, 3, 4, 3, 4, 4, 4, 4, 5, 4, 4, 3, 4, 5, 3, 4, 4],
            "handicaps": [11, 5, 17, 9, 7, 1, 3, 15, 13, 4, 12, 14, 16, 2, 6, 18, 8, 10],
        },
    ]
    config.get_logger().info("Inserting courses into database")
    for course in courses:
        client.table("course").insert(course).execute()


def get_course_by_name(client, course_name):
    response = client.table("course").select("*").eq("name", course_name).execute()
    if response.data:
        return response.data[0].get("id")
    else:
        return None
