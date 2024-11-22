from tkinter import *
import customtkinter as ctk
import rec_db   
import formatting



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
def dis(cmd=None, dset=None):
    if cmd == "select-players":
        players = rec_db.query_player(set(dset))
    else:
        players = rec_db.query_all_players()
    
    # format and display
    labels = formatting.format_labels(players)
    for label in labels:
        display.insert(ctk.END, label)



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
    if chars:
        dis(cmd="select-players", dsets=chars)
    else:
        # redisplay original
        dis()

ctk.CTkLabel(frame, text="Search").pack()
search_bar = ctk.CTkEntry(frame)
search_bar.pack()
search_bar.bind("<KeyRelease>", search)



# new player
def new_player():
    num = playerNumberEntry.get().strip()
    playerNumberEntry.delete(0, ctk.END)

    first = firstNameEntry.get().strip()
    firstNameEntry.delete(0, ctk.END)

    last = lastNameEntry.get().strip()
    lastNameEntry.delete(0, ctk.END)

    div = divisionEntry.get().strip()
    divisionEntry.delete(0, ctk.END)

    coach = coachEntry.get().strip()
    coachEntry.delete(0, ctk.END)

    rec_db.insert_player(num, first, last, div, coach)
    dis(cmd="select-players", dset=first)

# data fields
playerNumberEntry = ctk.CTkEntry(frame, placeholder_text="Player Number #")
playerNumberEntry.pack()
firstNameEntry = ctk.CTkEntry(frame, placeholder_text="First Name")
firstNameEntry.pack()
lastNameEntry = ctk.CTkEntry(frame, placeholder_text="Last Name")
lastNameEntry.pack()
divisionEntry = ctk.CTkEntry(frame, placeholder_text="Division")
divisionEntry.pack()
coachEntry = ctk.CTkEntry(frame, placeholder_text="Coach")
coachEntry.pack()

newPlayer_btn = ctk.CTkButton(frame, text="Add Player", command=new_player)
newPlayer_btn.pack()
newPlayer_btn.bind("<Return>", new_player)



# run
dis()
frame.mainloop()