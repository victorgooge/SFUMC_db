import tkinter as tk
import customtkinter as ctk
import test_frame as tf

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
u6_btn = ctk.CTkButton(frame, text="U6", command=lambda: tf.new_frame("U6"))
u6_btn.pack()
u8_btn = ctk.CTkButton(frame, text="U8", command=lambda: tf.new_frame("U8"))
u8_btn.pack()
u11_btn = ctk.CTkButton(frame, text="U11", command=lambda: tf.new_frame("U11"))
u11_btn.pack()
u14_btn = ctk.CTkButton(frame, text="U14", command=lambda: tf.new_frame("U14"))
u14_btn.pack()
# (players, coaches) - btn widgets
players_btn = ctk.CTkButton(frame, text="All Players", command=lambda: tf.new_frame("all_players"))
players_btn.pack()
coaches_btn = ctk.CTkButton(frame, text="All Coaches", command=lambda: tf.new_frame("all_coaches"))
coaches_btn.pack()
# all / whole db - btn widget
viewAll_btn = ctk.CTkButton(frame, text="View All", command=lambda: tf.new_frame("all"))
viewAll_btn.pack()

# run
frame.mainloop()