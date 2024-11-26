import customtkinter as ctk
from tkinter import ttk
import rec_db  



# initialize CustomTkinter
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  
# create main root window
root = ctk.CTk()
root.title("Modern CTk Table")
root.geometry("700x400")



# main Frame (contains all subframes)
main_frame = ctk.CTkFrame(root, fg_color="#2e2e2e")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)
# table Frame (for TreeView)
table_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
table_frame.pack(fill="both", expand=True, pady=(10, 0))



# TreeView (Table)
tree = ttk.Treeview(
    table_frame,
    columns=("Jersey #", "First Name", "Last Name", "Division", "Coach"),
    show="headings",
)

# define headings and columns
columns = ("Jersey #", "First Name", "Last Name", "Division", "Coach")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150 if col != "Jersey #" else 50)

# TreeView styling
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview",
    background="#2e2e2e",
    foreground="white",
    rowheight=30,
    fieldbackground="#2e2e2e",
    borderwidth=0,
)
style.configure(
    "Treeview.Heading",
    background="#5f6060",
    foreground="white",
    font=("Arial", 12, "bold"),
    borderwidth=0,
)
style.map("Treeview", background=[("selected", "#1a73e8")], foreground=[("selected", "white")])

# pack TreeView into table frame
tree.pack(fill="both", expand=True)

# button frame (for actions and search)
button_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
button_frame.pack(fill="x", pady=10)



# frame when adding player data 
def show_add_player_frame():
    # create add player frame
    add_frame = ctk.CTkFrame(root, fg_color="#2e2e2e")
    add_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # input fields for player data
    ctk.CTkLabel(add_frame, text="Add New Player", font=("Arial", 16, "bold")).pack(pady=10)
    player_number = ctk.CTkEntry(add_frame, placeholder_text="Player Number #")
    player_number.pack(pady=5)
    first_name = ctk.CTkEntry(add_frame, placeholder_text="First Name")
    first_name.pack(pady=5)
    last_name = ctk.CTkEntry(add_frame, placeholder_text="Last Name")
    last_name.pack(pady=5)

    # dropdown for divisions
    division_options = ["U6", "U8", "U12", "U16"]  # divisions
    division = ctk.CTkOptionMenu(
        add_frame, 
        values=division_options,
        fg_color="#666562",
        button_color="#403f3e",
        button_hover_color="#adadac",
        dropdown_fg_color="#666562",
        dropdown_hover_color="#adadac"
    )
    division.set("Select Division")  
    division.pack(pady=5)

    # dropdown for coaches
    coach_options = ["Carlos", "Aria", "Lionel", "William"]  # coaches
    coach = ctk.CTkOptionMenu(
        add_frame, 
        values=coach_options,
                fg_color="#666562",
        button_color="#403f3e",
        button_hover_color="#adadac",
        dropdown_fg_color="#666562",
        dropdown_hover_color="#adadac"
    )
    coach.set("Select Coach")  
    coach.pack(pady=5)

    # submit data to db and tree
    def submit(event=None):
        # add player to database and table
        rec_db.insert_player(
            player_number.get().strip(),
            first_name.get().strip(),
            last_name.get().strip(),
            division.get(), 
            coach.get(),    
        )
        tree.insert("", "end", values=(
            player_number.get().strip(),
            first_name.get().strip(),
            last_name.get().strip(),
            division.get(),
            coach.get(),
        ))
        division.set("Select Division")
        coach.set("Select Coach")

        # switch back to main frame
        add_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        display()

    submit_btn = ctk.CTkButton(add_frame, text="Submit", command=submit)
    submit_btn.pack(pady=10)

    root.bind("<Return>", submit)

    # back 
    def back():
        # hide add frame and show main frame
        add_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)

    ctk.CTkButton(add_frame, text="Back", command=back).pack(pady=5)

    # hide main frame and show add frame
    main_frame.pack_forget()
    add_frame.pack(fill="both", expand=True)




# widgets in button frame
add_button = ctk.CTkButton(button_frame, text="Add Item", corner_radius=8, command=show_add_player_frame)
add_button.pack(side="left", padx=10)

# delete player(s) from db and remove from tree
def delete(event=None):
    selected_items = tree.selection()
    to_delete = []
    for item in selected_items:
        values = tree.item(item, "values")
        to_delete.append((values[1], values[2]))  # db data: 1 - first_name, 2 - last_name
    if to_delete:
        rec_db.delete_player(to_delete)
        display()
# delete Button
delete_button = ctk.CTkButton(button_frame, text="Delete Item", corner_radius=8, command=delete)
delete_button.pack(side="left", padx=10)
tree.bind("<BackSpace>", delete)

# widget functionality
# search bar
def search(event=None):
    query = search_entry.get().strip()
    if query:
        display(cmd="select-players", dset=query)
    else:
        display()

search_entry = ctk.CTkEntry(button_frame, placeholder_text="Search")
search_entry.pack(side="left", fill="x", expand=True, padx=10)
search_entry.bind("<KeyRelease>", search)



# display data from db into tree table
def display(cmd=None, dset=None):
    for item in tree.get_children():
        tree.delete(item)
    if cmd == "select-players":
        data = rec_db.query_player(dset)
    else:
        data = rec_db.query_all_players()
    for row in data:
        tree.insert("", "end", values=row)



# exe
display()
root.mainloop()
