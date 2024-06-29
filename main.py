import tkinter as tk
import customtkinter as ctk
import sqlite3


# gui settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# window frame
frame = ctk.CTk()
frame.title("SFUMC REC Soccer")

'''main screen layout (static)'''
# teams - title widget
title = ctk.CTkLabel(frame, text="TEAMS")
title.pack() 
# (u6 u8 u11 u14) - btn widgets
u6_btn = ctk.CTkButton(frame, text="U6")
u6_btn.pack()
u8_btn = ctk.CTkButton(frame, text="U8")
u8_btn.pack()
u11_btn = ctk.CTkButton(frame, text="U11")
u11_btn.pack()
u14_btn = ctk.CTkButton(frame, text="U14")
u14_btn.pack()
# (players, coaches) - btn widgets
players_btn = ctk.CTkButton(frame, text="Players")
players_btn.pack()
coaches_btn = ctk.CTkButton(frame, text="Coaches")
coaches_btn.pack()

# run
frame.mainloop()