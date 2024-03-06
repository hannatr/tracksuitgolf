# Track Suit Golf

Database population script and demo Next.js app connecting to it. Uses Supabase.

## Setup

  - Run `poetry install` (Requires Python 3.11+).
  - Setup Supabase application. Run `migrations/001_create_tables.sql` to create database.
  - Obtain Supabase URL and Key. Update `data/config.ini` with URL. Export key to environment variable `SUPABASE_KEY`.
  - Populate database with API script: `poetry run python3 -m tsg_api.main`.
  - Start frontend with `cd tracksuitgolf; npm install;`.
  - Create `tracksuitgolf/.env.local` and populate with contents below.
  - Star sample web app with `npm run dev`.

### .env.local file

```
NEXT_PUBLIC_SUPABASE_URL=<url>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<key>
```

## TODO
 
  - Schema: put a current score(s) on the matches
  - Schema: Security on SQL
  - Score Update Function: Update a hole score, calculate scores
