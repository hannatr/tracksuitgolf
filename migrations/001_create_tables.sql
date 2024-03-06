CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    current_handicap DECIMAL NOT NULL
);

CREATE TABLE course (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    pars INTEGER[] NOT NULL,
    handicaps INTEGER[] NOT NULL
);

CREATE TABLE tournament (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    year INTEGER NOT NULL,
    team_1 INTEGER[] NOT NULL, -- References Player IDs
    team_2 INTEGER[] NOT NULL, -- References Player IDs
    team_1_score DECIMAL NOT NULL DEFAULT 0,
    team_2_score DECIMAL NOT NULL DEFAULT 0
);

CREATE TABLE scorecard (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES Player(id),
    course_id INTEGER REFERENCES Course(id),
    date_played DATE NOT NULL,
    playing_hcp DECIMAL NOT NULL,
    strokes INTEGER[] NOT NULL
);

CREATE TABLE match (
    id SERIAL PRIMARY KEY,
    tournament_id INTEGER REFERENCES Tournament(id),
    scoring_type TEXT NOT NULL,
    team_1_scorecards INTEGER[] NOT NULL, -- References Scorecard IDs
    team_2_scorecards INTEGER[] NOT NULL -- References Scorecard IDs
);
