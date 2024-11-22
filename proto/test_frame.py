import customtkinter as ctk
import rec_db

def new_frame(cat):
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
        players = rec_db.query_all_players()
        coaches = rec_db.query_all_coaches()
        display.delete('1.0', ctk.END) 

        def iter(cond=None):
            if cond:
                for player in players:
                    if player[3] == cond:
                        display.insert(ctk.END, f"#{player[0]}    {player[2].upper()}, {player[1]}:    {player[3]} - {player[4]}\n\n")
            else:
                display.insert(ctk.END, "PLAYERS\n")
                display.insert(ctk.END, "--------------------------------------------------------------------\n")
                for player in players:
                    display.insert(ctk.END, f"#{player[0]}    {player[2].upper()}, {player[1]}:    {player[3]} - {player[4]}\n\n")
                
                display.insert(ctk.END, "COACHES\n")
                display.insert(ctk.END, "--------------------------------------------------------------------\n")
                for coach in coaches:
                    display.insert(ctk.END, f"{coach[1]}    {coaches[2]}, {coaches[3]}, {coaches[4]}\n\n")

        if cat == 'all':
            iter()
        elif cat == 'all_players':
            pass
        elif cat == 'all_coaches':
            pass 
        else:
            iter(cat)
            

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