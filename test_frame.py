import customtkinter as ctk
import rec_db

frame = ctk.CTk()

display = ctk.CTkTextbox(frame, width=600, height=300, font=("Helvetica", 16))
display.pack()

playerNum_entry = ctk.CTkEntry(frame, placeholder_text="Number")
playerNum_entry.pack()
firstName_entry = ctk.CTkEntry(frame, placeholder_text="First Name")
firstName_entry.pack()
lastName_entry = ctk.CTkEntry(frame, placeholder_text="Last Name")
lastName_entry.pack()
division_entry = ctk.CTkEntry(frame, placeholder_text="Divsion (Ex: U11)")
division_entry.pack()
coach_entry = ctk.CTkEntry(frame, placeholder_text="Coach")
coach_entry.pack()

def dis():
    # query all players and display them
    players = rec_db.query_all()
    display.delete('1.0', ctk.END) 
    for player in players:
        display.insert(ctk.END, f"#{player[0]}    {player[2].upper()}, {player[1]}:    {player[3]} - {player[4]}\n\n")

def add():
    rec_db.insert_player(num=playerNum_entry.get(), fn=firstName_entry.get(), ln=lastName_entry.get(), div=division_entry.get(), coach=coach_entry.get())
    dis()
    playerNum_entry.delete(0, ctk.END)
    firstName_entry.delete(0, ctk.END)
    lastName_entry.delete(0, ctk.END)
    division_entry.delete(0, ctk.END)
    coach_entry.delete(0, ctk.END)


addPlayer_btn = ctk.CTkButton(frame, text="Add Player", command=add)
addPlayer_btn.pack()

# display all prior data
dis()

frame.mainloop()