import tkinter as tk
import customtkinter as ctk
import proto.test_frame as tf
import rec_db   

# gui settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# window frame
frame = ctk.CTk()
frame.title("SFUMC REC Soccer")
title = ctk.CTkLabel(frame, text="REC Database")
title.pack() 

# textbox display
display = ctk.CTkTextbox(frame, width=600, height=300, font=("Helvetica", 16))
display.pack()

# player display
def dis(cmd=None, s=None):
    if cmd == "select-players":
         players = rec_db.query_player(set(s))
    else:
        players = rec_db.query_all_players()

    for player in players:
            display.insert(ctk.END, f"#{player[0]}    {player[1]}, {player[2].upper()}:    {player[3]} - {player[4]}\n\n")



# filter settings
ctk.CTkLabel(frame, text="Filter").pack()
# check func
def checkbox_event():
    ctk.CTkLabel(frame, text="<action>").pack()
# checkboxes
checkbox1 = ctk.CTkCheckBox(master=frame, text="Division", command=checkbox_event)
checkbox1.pack()
checkbox2 = ctk.CTkCheckBox(master=frame, text="Team", command=checkbox_event)
checkbox2.pack()
checkbox3 = ctk.CTkCheckBox(master=frame, text="Coach", command=checkbox_event)
checkbox3.pack()



# search bar
def search(event=None):
    display.delete('1.0', ctk.END) 
    # first query names containing chars
    chars = search_bar.get().strip()
    print(chars)
    if chars:
        dis(cmd="select-players", s=chars)
    else:
        # redisplay original
        dis()

ctk.CTkLabel(frame, text="Search").pack()
search_bar = ctk.CTkEntry(frame)
search_bar.pack()
search_bar.bind("<KeyRelease>", search)



# run
dis()
frame.mainloop()