-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--DROP table players;

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament

--DROP table players;

CREATE TABLE players (
    id serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE matches (
    player_id integer REFERENCES players(id) ON DELETE CASCADE,
    wins integer DEFAULT 0,
    matches integer DEFAULT 0
);

-- Views --
CREATE VIEW newPlayerId AS
    SELECT id FROM players ORDER BY id DESC LIMIT 1;


CREATE VIEW players_standings AS
    SELECT players.id, players.name, matches.wins, matches.matches
    FROM players, matches WHERE players.id = matches.player_id ORDER BY matches.wins
    DESC, matches.matches DESC;