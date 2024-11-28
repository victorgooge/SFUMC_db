import sqlite3
import pandas as pd

# db
conn = sqlite3.connect('sfumc_rec.db')
cursor = conn.cursor()



# players table
c1 = """CREATE TABLE IF NOT EXISTS 
players(player_number INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, division INTEGER, coach TEXT)""" # NOTE: Mispelled division when initzializing
cursor.execute(c1)

# insert player function
def insert_player(num, fn, ln, div, coach):
    cursor.execute("INSERT INTO players (player_number, first_name, last_name, division, coach) VALUES (?, ?, ?, ?, ?)",
                   (num, fn, ln, div, coach))
    conn.commit() 
# query all players
def query_all_players(sort_filter):
    if sort_filter == "Name [Z-A]":
        cursor.execute("SELECT * FROM players ORDER BY first_name DESC")
    elif sort_filter == "Number":
         cursor.execute("SELECT * FROM players ORDER BY player_number")
    elif sort_filter == "Division":
        cursor.execute("SELECT * FROM players ORDER BY divsion DESC") # NOTE: SPELLING ERROR IN for division col
        # NOTE: make data field strictly integer type
    elif sort_filter == "Coach":
        cursor.execute("SELECT * FROM players ORDER BY coach")
    else:
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
# deleting player(s)
def delete_player(to_delete):
        name_tuples = [(name[0], name[1]) for name in to_delete]
        placeholders = ",".join(["(?, ?)"] * len(name_tuples))
        query = f"DELETE FROM players WHERE (first_name, last_name) IN ({placeholders})"
        cursor.execute(query, [item for sublist in name_tuples for item in sublist])
        conn.commit()

# # generat xlsx
# def export_to_excel():
#     query = "SELECT * FROM players"
#     df = pd.read_sql_query(query, conn)  # Fetch data as a DataFrame
#     output_file = "players_data.xlsx"
#     df.to_excel(output_file, index=False, engine='openpyxl')  # Save DataFrame to Excel

     



# coaches table
c2 = """CREATE TABLE IF NOT EXISTS
coaches(INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, division INTEGER, team TEXT)"""
cursor.execute(c2)

# query all coaches
def query_all_coaches():
    cursor.execute("SELECT * FROM coaches")
    return cursor.fetchall() 
# query player
def query_coach(fn, ln):
    cursor.execute("SELECT * FROM coaches WHERE first_name = ? AND last_name = ?", (fn, ln))
    return cursor.fetchall() 
