import sqlite3
import pandas as pd
from tkinter import filedialog

# db
conn = sqlite3.connect('sfumc_rec.db')
cursor = conn.cursor()



# players table
c1 = """CREATE TABLE IF NOT EXISTS 
players(player_number INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, division INTEGER, coach TEXT)"""
cursor.execute(c1)

# check if the players table is empty
def is_players_table_empty():
    cursor.execute("SELECT COUNT(*) FROM players")
    return cursor.fetchone()[0] == 0
# import data from Excel to the database
def import_from_excel(file_path):
    try:
        # read excel file
        df = pd.read_excel(file_path, engine='openpyxl')
        df.rename(
            columns={
                "Player Number": "player_number",
                "First Name": "first_name",
                "Last Name": "last_name",
                "Division": "division",
                "Coach": "coach"
            },
            inplace=True
        )

        # insert data into players table
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT OR IGNORE INTO players (player_number, first_name, last_name, division, coach) VALUES (?, ?, ?, ?, ?)",
                (row["player_number"], row["first_name"], row["last_name"], row["division"], row["coach"]),
            )
        conn.commit()
    except Exception as e:
        raise ValueError(f"Failed to import data from Excel: {e}")
# insert player function
def insert_player(num, fn, ln, div, coach):
    cursor.execute("INSERT INTO players (player_number, first_name, last_name, division, coach) VALUES (?, ?, ?, ?, ?)",
                   (num, fn, ln, div, coach))
    conn.commit() 
# query all players
def query_all_players(sort_filter=None):
    if sort_filter == "Name [Z-A]":
        cursor.execute("SELECT * FROM players ORDER BY first_name DESC")
    elif sort_filter == "Number":
         cursor.execute("SELECT * FROM players ORDER BY player_number")
    elif sort_filter == "Division":
        cursor.execute("SELECT * FROM players ORDER BY division DESC") 
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

# generat xlsx
def export_to_excel():
    try:
        # prompt user to select location and file name for saving
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Save Excel File As"
        )

        # if user cancels, do nothing
        if not file_path:
            return

        # query database
        query = "SELECT * FROM players"
        df = pd.read_sql_query(query, conn)  # fetch data as dataframe

        # save dataframe to specified file
        df.to_excel(file_path, index=False, engine='openpyxl')

        print(f"Data successfully exported to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

     



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
