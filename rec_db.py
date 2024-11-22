import sqlite3

# db
conn = sqlite3.connect('sfumc_rec.db')
cursor = conn.cursor()



# players table
c1 = """CREATE TABLE IF NOT EXISTS 
players(player_number INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, divsion INTEGER, coach TEXT)"""
cursor.execute(c1)

# insert player function
def insert_player(num, fn, ln, div, coach):
    cursor.execute("INSERT INTO players (player_number, first_name, last_name, divsion, coach) VALUES (?, ?, ?, ?, ?)",
                   (num, fn, ln, div, coach))
    conn.commit() 
# query all players
def query_all_players():
    cursor.execute("SELECT * FROM players ORDER BY first_name")
    return cursor.fetchall() 
# query player
def query_player(chars):
        query_conditions = []
        params = []
        
        for char in chars:
            query_conditions.append("first_name LIKE ?")
            params.append(f"%{char}%")
        
        # combine conditions with AND
        query = f"SELECT * FROM players WHERE {' AND '.join(query_conditions)} ORDER BY first_name"
        
        cursor.execute(query, params)
        return cursor.fetchall()



# coaches table
c2 = """CREATE TABLE IF NOT EXISTS
coaches(INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, divsion INTEGER, team TEXT)"""
cursor.execute(c2)

# query all coaches
def query_all_coaches():
    cursor.execute("SELECT * FROM coaches")
    return cursor.fetchall() 
# query player
def query_coach(fn, ln):
    cursor.execute("SELECT * FROM coaches WHERE first_name = ? AND last_name = ?", (fn, ln))
    return cursor.fetchall() 
