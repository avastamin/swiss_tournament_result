#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
from contextlib import contextmanager
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection failed")

@contextmanager
def get_cursor():
    """
    Query helper function using context lib. Creates a cursor from a database
    connection object, and performs queries using that cursor.
    """
    DB = connect()
    cursor = DB.cursor()
    try:
        yield cursor
    except:
        raise
    else:
        DB.commit()
    finally:
        cursor.close()
        DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM matches")

def deletePlayers():
    """Remove all the player records from the database."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM players")

def countPlayers():
    """Returns the number of players currently registered."""
    with get_cursor() as cursor:
        cursor.execute("SELECT count(*)  FROM players")
        numberofplayers = cursor.fetchone()[0]
        return numberofplayers


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO players (name) VALUES (%s)", (name, ))

        cursor.execute("SELECT id FROM newPlayerID")
        latest_player_id = cursor.fetchone()
        cursor.execute("INSERT INTO matches VALUES (%s)", (latest_player_id,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM players_standings")
        playerstandings = cursor.fetchall()
        return playerstandings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with get_cursor() as cursor:

        cursor.execute("UPDATE matches set matches = matches +1"
                 "WHERE player_id = %s OR player_id = %s", (winner, loser, ))

        cursor.execute("UPDATE matches set wins = wins +1"
                "WHERE player_id = %s", (winner,))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with get_cursor() as cursor:

        cursor.execute("SELECT id, name FROM players_standings")
        all_players = cursor.fetchall()

    swisspairs = [ ]
    while all_players:
         swisspairs.append(all_players[0] + all_players[1])
         del all_players[0:2]

    return swisspairs



def toseeRecords():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM matches")
        latest_player_id = cursor.fetchall()
        return latest_player_id

#print reportMatch(32,31)
print (toseeRecords())
#deleteMatches()
#deletePlayers()
registerPlayer('playerA')
registerPlayer('playerB')
registerPlayer('playerC')
registerPlayer('playerD')

