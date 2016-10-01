# Swiss Tournament Game Result

## Task reqierments:
you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a Swiss system game tournament.
This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

## File structure
**tournament.sql** for database schema.
**tournament.py** main python file which contains all functions
**tournament_test.py** python file to verify the code

## Functions in tournament.py

**registerPlayer(name)**
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

**deletePlayers()**
Clear out all the player records from the database.

**reportMatch(winner, loser)**
Stores the outcome of a single match between two players in the database.
 Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

**deleteMatches()**
Clear out all the match records from the database.

**playerStandings()**
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

**swissPairings()**
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
## System requirements:
- PostgreSQL
- Python 2.7

# Clone the git repository and cd into your desired folder of the cloned directory.
git clone https://github.com/avastamin/swiss_tournament_result.git

# run sql to create the database schema
psql -f tournaments.sql

# to run tests, tournaments_test.py
python tournaments_test.py
