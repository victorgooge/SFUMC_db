import tkinter as tk
import customtkinter as ctk
import test_frame as tf

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
ctk.CTkLabel(frame, text="Search").pack()
search_bar = ctk.CTkEntry(frame)
search_bar.pack()


frame.mainloop()