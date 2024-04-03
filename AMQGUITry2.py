import tkinter as tk
from tkinter import filedialog
import customtkinter
import AMQFolderReader
import AMQRatioCalc

# GLOBALS
bg = "#49A078"
ratio_returned_list = []
current_ratio_entry_index = 0
ratio_current_entry_frame = None
current_ratio_entry_label = None

# Setting up root
root = customtkinter.CTk(fg_color=bg)
root.title("Time Chamber Test Branch")
root.eval("tk::PlaceWindow . center")
root.geometry("500x570")
root.configure(background=bg)

user_master_dict = {}


def main_menu_frame_load():
    # Functions
    def destroy_frame():
        master_main_menu_frame.destroy()

    # Master MM Frame
    master_main_menu_frame = tk.Frame(root, width=500, height=570, bg=bg)
    master_main_menu_frame.pack()
    master_main_menu_frame.pack_propagate(False)

    # First frame
    main_menu_frame = tk.Frame(master_main_menu_frame, width=500, height=570, bg=bg)
    main_menu_frame.pack()
    main_menu_frame.pack_propagate(False)

    # Second MM Frame
    main_menu_subtitle_frame = tk.Frame(master_main_menu_frame, bg=bg)
    main_menu_subtitle_frame.pack()
    main_menu_subtitle_frame.pack_propagate(False)

    # MM Buttons Frame
    main_menu_buttons_frame = tk.Frame(master_main_menu_frame, bg=bg)
    main_menu_buttons_frame.pack()
    main_menu_buttons_frame.pack_propagate(False)
    # Title
    menu_title1 = tk.Label(
        main_menu_frame,
        text="Yoav",
        bg=bg,
        fg="#47F4BB",
        font=("Lemon/Milk", 20)
    )
    menu_title2 = tk.Label(
        main_menu_frame,
        text="'s AMQ Time Chamber",
        bg=bg,
        fg="#9CC5A1",
        font=("Lemon/Milk", 24)
    )

    submenu_title1 = tk.Label(
        main_menu_subtitle_frame,
        text="Graphical",
        bg=bg,
        fg="#9CC5A1",
        font=("Lemon/Milk", 12)
    )

    submenu_title2 = tk.Label(
        main_menu_subtitle_frame,
        text="User Interface",
        bg=bg,
        fg="#9CC5A1",
        font=("Lemon/Milk", 12)
    )

    submenu_title3 = tk.Label(
        main_menu_subtitle_frame,
        text="Version",
        bg=bg,
        fg="#9CC5A1",
        font=("Lemon/Milk", 12)
    )

    menu_title_flavor = tk.Label(
        main_menu_subtitle_frame,
        text="(limited functionality)",
        bg=bg,
        fg="#47614A",
        font=("Lemon/Milk", 6)
    )

    # Title Packing
    menu_title1.grid(row=0, column=0, columnspan=2, pady=34, sticky="E")
    menu_title2.grid(row=0, column=2, columnspan=2, pady=34)
    submenu_title1.grid(row=1, column=0)
    submenu_title2.grid(row=1, column=1)
    submenu_title3.grid(row=1, column=2)
    menu_title_flavor.grid(row=2, column=0, columnspan=3, sticky="NE")

    # MM Buttons
    mm_space = tk.Label(main_menu_buttons_frame, pady=20, bg=bg)

    def button_database_command():
        destroy_frame()
        database_frame_load()

    button_database = customtkinter.CTkButton(main_menu_buttons_frame,
                                              text="Database",
                                              fg_color="#216869",
                                              height=80,
                                              width=200,
                                              font=("Ubuntu", 32),
                                              command=button_database_command)

    def button_database_command():
        destroy_frame()
        ratio_frame_load()

    button_ratios = customtkinter.CTkButton(main_menu_buttons_frame,
                                            text="Ratios",
                                            fg_color="#216869",
                                            height=80,
                                            width=200,
                                            font=("Ubuntu", 35),
                                            command=button_database_command)
    button_player_stats = customtkinter.CTkButton(main_menu_buttons_frame,
                                                  text="Player Stats",
                                                  fg_color="#216869",
                                                  height=80,
                                                  width=200,
                                                  font=("Ubuntu", 30))

    button_entry = customtkinter.CTkButton(main_menu_buttons_frame,
                                           text="Entry Lookup",
                                           fg_color="#216869",
                                           height=80,
                                           width=200,
                                           font=("Ubuntu", 27)
                                           )

    def button_user_folder_command():
        global user_master_dict

        user_dir = filedialog.askdirectory()
        user_master_dict = AMQFolderReader.make_master_dict(user_dir)

    button_user_folder = customtkinter.CTkButton(main_menu_buttons_frame,
                                                 text="Choose Folder Location",
                                                 fg_color="#216869",
                                                 height=40,
                                                 width=412,
                                                 font=("Ubuntu", 27),
                                                 command=button_user_folder_command
                                                 )

    # Buttons Packing
    mm_space.grid(row=0, column=0, columnspan=2, pady=50)
    button_database.grid(row=1, column=0, padx=6, pady=6)
    button_ratios.grid(row=1, column=1, padx=6, pady=6)
    button_player_stats.grid(row=2, column=0, padx=6, pady=6)
    button_entry.grid(row=2, column=1, padx=6, pady=6)
    button_user_folder.grid(row=3, column=0, columnspan=2, pady=6)


def database_frame_load():
    """
    Loads the database frame onto the main window.
    WARNING: OUTDATED AND SLOW, the ratio frame contains all the functionality
    of the database frame and works much faster, there is no longer a use for this frame.
    """
    global user_master_dict

    # Frames
    database_master_frame = tk.Frame(root, bg=bg)
    database_master_frame.pack()
    database_input_frame = customtkinter.CTkScrollableFrame(database_master_frame,
                                                            height=300,
                                                            width=400,
                                                            orientation="vertical")
    database_input_frame.grid(column=0, row=1)

    # Widgets
    entry_title = tk.Label(database_master_frame,
                           text="Database",
                           font=("Lemon/Milk", 24),
                           fg="#9CC5A1",
                           bg=bg)
    entry_title.grid(column=0, row=0, pady=34)

    element_count = 0
    for song in user_master_dict:
        database_song_output = tk.Label(database_input_frame, text=song, font=("Ubuntu", 12))
        database_song_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        for element in user_master_dict[song]["info"]:
            print(element)

        database_element_output = tk.Label(database_input_frame,
                                           text="Song: " + str(user_master_dict[song]["info"]["songName"]) +
                                                "   Artist: " + str(user_master_dict[song]["info"]["artist"]),
                                           font=("Ubuntu", 7),
                                           bg="red")
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Anime name: " + str(user_master_dict[song]["info"]["animeNames"]),
                                           font=("Ubuntu", 7),
                                           bg="red")
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Alt Anime Names: " + str(
                                            user_master_dict[song]["info"]["altAnimeNames"]) +
                                           " Alt Anime Name Answers: " +
                                           str(user_master_dict[song]["info"]["altAnimeNamesAnswers"])
                                           )
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Type: " + str(user_master_dict[song]["info"]["type"]) +
                                                " Type Number: " + str(user_master_dict[song]["info"]["typeNumber"]) +
                                                " ANN ID: " + str(user_master_dict[song]["info"]["annId"]) +
                                                " High Risk: " + str(user_master_dict[song]["info"]["highRisk"]) +
                                                " Anime Score: " + str(user_master_dict[song]["info"]["animeScore"]) +
                                                " Anime Type: " + str(user_master_dict[song]["info"]["animeType"]) +
                                                " " + str(user_master_dict[song]["info"]["vintage"]),
                                           font=("Ubuntu", 7),
                                           bg="red")
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Difficulty: " + str(user_master_dict[song]["info"]["animeDifficulty"])[
                                                                 :5] +
                                                " Genre: " + str(user_master_dict[song]["info"]["animeGenre"]))
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Site IDs: " + str(user_master_dict[song]["info"]["siteIds"]))
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="Tags: " + str(user_master_dict[song]["info"]["animeTags"]))
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        element_count += 1

        database_element_output = tk.Label(database_input_frame,
                                           text="correct: " + str(user_master_dict[song]["correct"]) + " incorrect: " +
                                                str(user_master_dict[song]["incorrect"]),
                                           font=("Ubuntu", 7),
                                           bg="yellow")
        database_element_output.grid(column=0, row=element_count, sticky="W", pady=5)
        database_element_output = tk.Label(database_input_frame,
                                           text=user_master_dict[song]["incorrect"],
                                           font=("Ubuntu", 7),
                                           bg="blue")
        database_element_output.grid(column=1, row=element_count, sticky="W", pady=5)
        element_count += 1


def ratio_frame_load():
    """
    The ratio frame, displays all loaded entries one by one.
    Can load all loaded entries, every entry from a specific show, and a specific song ID's entry.
    Can filter entries by minimum times of appearance, and by maximum ratio of correct guesses.
    """
    global current_ratio_entry_label
    global user_master_dict
    global ratio_current_entry_frame
    # Frames
    ratio_master_frame = tk.Frame(root, bg=bg)

    # Frame all
    ratio_master_frame.pack()
    ratio_entries_frame = customtkinter.CTkScrollableFrame(ratio_master_frame,
                                                           height=270,
                                                           width=400,
                                                           orientation="horizontal",
                                                           fg_color="#1f2421")
    ratio_entries_frame.grid(column=0, row=2, columnspan=4)
    # Widgets
    entry_title = tk.Label(ratio_master_frame,
                           text="Ratios",
                           font=("Lemon/Milk", 24),
                           fg="#9CC5A1",
                           bg=bg)
    entry_title.grid(column=0, row=0, columnspan=4, pady=34)
    # MAKING THE INPUT SECTION!!!
    input_line_widget = customtkinter.CTkEntry(ratio_master_frame, height=5, width=200)
    input_line_widget.grid(row=1, column=0, columnspan=2)

    # Dropdown menu options
    options = [
        "Generate All",
        "Song ID",
        "Anime Name",
    ]
    # datatype of menu text
    drop = customtkinter.CTkComboBox(ratio_master_frame, values=options)
    drop.grid(row=1, column=2, columnspan=2, padx=5, sticky="WE")

    def ratios_get():
        global ratio_returned_list
        global current_ratio_entry_index
        global current_ratio_entry_label
        global user_master_dict

        user_input_method = ""
        user_textbox_input = input_line_widget.get()
        if drop.get() == options[0]:
            user_input_method = None
        elif drop.get() == options[1]:
            user_input_method = "id"
        elif drop.get() == options[2]:
            user_input_method = "anime_name"
        ratio_returned_list = AMQRatioCalc.total_ratio_return(user_master_dict,
                                                              user_textbox_input,
                                                              user_input_method,
                                                              min_entries=min_entries_entry.get(),
                                                              max_ratio=max_ratio_entry.get())
        current_ratio_entry_index = 0
        if ratio_returned_list:
            current_ratio_entry_label.configure(text=f"{current_ratio_entry_index + 1} / {len(ratio_returned_list)}")
            load_current_entry_frame()

    # Buttons Frame
    ratio_parameters_frame = customtkinter.CTkFrame(ratio_master_frame, fg_color=bg)
    ratio_parameters_frame.grid(row=4, column=0, columnspan=4, sticky="WE", pady=5)

    # Ratio calc buttons
    load_button = customtkinter.CTkButton(ratio_parameters_frame,
                                          text="Load",
                                          font=("Lemon/Milk", 20),
                                          height=30,
                                          fg_color="#216869",
                                          command=ratios_get)
    customtkinter.CTkLabel(ratio_parameters_frame,
                           text="Min. Entries:",
                           font=("Lemon/Milk", 15)).grid(row=0, column=0)
    min_entries_entry = customtkinter.CTkEntry(ratio_parameters_frame, height=5, width=30, placeholder_text="1")
    min_entries_entry.grid(row=0, column=1, padx=5)

    customtkinter.CTkLabel(ratio_parameters_frame,
                           text="Max. Ratio:",
                           font=("Lemon/Milk", 15)).grid(row=0, column=2)
    max_ratio_entry = customtkinter.CTkEntry(ratio_parameters_frame, height=5, width=30, placeholder_text="1.0")
    max_ratio_entry.grid(row=0, column=3, padx=5)
    load_button.grid(row=0, column=4)
    ratio_controls_frame = customtkinter.CTkFrame(ratio_master_frame, fg_color=bg)
    ratio_controls_frame.grid(row=5, column=0, columnspan=4, sticky="WE", pady=5)

    # Swap Song Buttons
    def ratio_prev_button_func():
        global ratio_returned_list
        global current_ratio_entry_index
        global current_ratio_entry_label

        if current_ratio_entry_index > len(ratio_returned_list):
            current_ratio_entry_index = 0
        elif current_ratio_entry_index > 0:
            current_ratio_entry_index -= 1
        current_ratio_entry_label.configure(text=f"{current_ratio_entry_index + 1} / {len(ratio_returned_list)}")
        # print(ratio_returned_list)
        load_current_entry_frame()

    prev_ratio_entry_button = customtkinter.CTkButton(ratio_controls_frame,
                                                      text="<--",
                                                      fg_color="#216869",
                                                      height=40,
                                                      font=("Ubuntu", 26),
                                                      command=ratio_prev_button_func
                                                      )
    prev_ratio_entry_button.grid(row=0, column=0)

    def ratio_next_button_func():
        global ratio_returned_list
        global current_ratio_entry_index
        if current_ratio_entry_index > len(ratio_returned_list):
            current_ratio_entry_index = 0
        elif current_ratio_entry_index + 1 < len(ratio_returned_list):
            current_ratio_entry_index += 1
        current_ratio_entry_label.configure(text=f"{current_ratio_entry_index + 1} / {len(ratio_returned_list)}")
        load_current_entry_frame()

    next_ratio_entry_button = customtkinter.CTkButton(ratio_controls_frame,
                                                      text="-->",
                                                      fg_color="#216869",
                                                      height=40,
                                                      font=("Ubuntu", 26),
                                                      command=ratio_next_button_func
                                                      )
    next_ratio_entry_button.grid(row=0, column=1, padx=10)

    current_ratio_entry_label = tk.Label(ratio_controls_frame,
                                         text="pls load",
                                         font=("Lemon/Milk", 15),
                                         fg="#9CC5A1",
                                         bg=bg)
    current_ratio_entry_label.grid(row=0, column=2)
    ratio_current_entry_frame = customtkinter.CTkFrame(ratio_entries_frame, fg_color="#1f2421")
    ratio_current_entry_frame.grid(row=0, column=0, sticky="NEWS")

    def load_current_song_info():
        """
        popup window containing a song's full info
        """
        global user_master_dict

        # Base Window Properties
        top = tk.Toplevel()
        top.geometry("500x300")
        top_frame = customtkinter.CTkScrollableFrame(top,
                                                     width=500,
                                                     height=300,
                                                     fg_color="#1f2421",
                                                     corner_radius=0,
                                                     orientation="horizontal")
        top_frame.pack()

        # Song Info Labels
        popup_song_id = tk.Label(top_frame,
                                 text="Full info for ID " + ratio_returned_list[current_ratio_entry_index]["id"] + ":",
                                 font=("Ubuntu", 22),
                                 bg="#1f2421",
                                 fg="#dce1de")
        popup_song_name = tk.Label(top_frame,
                                   text="Song Name: " + user_master_dict
                                   [ratio_returned_list
                                       [current_ratio_entry_index]
                                       ["id"]]["info"]["songName"])
        popup_anime_name_eng = tk.Label(top_frame,
                                        text="English Anime Name: " + user_master_dict
                                        [ratio_returned_list
                                            [current_ratio_entry_index]
                                            ["id"]]["info"]["animeNames"]["english"],
                                        font=("Ubuntu", 16),
                                        bg="#1f2421",
                                        fg="#dce1de")
        popup_anime_name_jp = tk.Label(top_frame,
                                       text="Japanese Anime Name: " + user_master_dict
                                       [ratio_returned_list
                                           [current_ratio_entry_index]
                                           ["id"]]["info"]["animeNames"]["romaji"],
                                       font=("Ubuntu", 16),
                                       bg="#1f2421",
                                       fg="#dce1de")
        popup_anime_name_alt = tk.Label(top_frame,
                                        text="Alt Anime Names: " +
                                             str(user_master_dict[ratio_returned_list[current_ratio_entry_index]["id"]]
                                                 ["info"]["altAnimeNames"]) +
                                             " Alt Anime Name Answers: " +
                                             str(user_master_dict
                                                 [ratio_returned_list[current_ratio_entry_index]
                                                 ["id"]]["info"]["altAnimeNamesAnswers"]),
                                        font=("Ubuntu", 16),
                                        bg="#1f2421",
                                        fg="#dce1de")
        popup_anime_stats = tk.Label(top_frame,
                                     text="Type: " + str(
                                         user_master_dict
                                         [ratio_returned_list[current_ratio_entry_index]["id"]]["info"]
                                         ["type"]) + " Type Number: " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["typeNumber"]) +
                                          " ANN ID: " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["annId"]) +
                                          " High Risk: " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["highRisk"]) +
                                          " Anime Score: " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["animeScore"]) +
                                          " Anime Type: " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["animeType"]) +
                                          " " + str(
                                         user_master_dict[ratio_returned_list[current_ratio_entry_index]
                                         ["id"]]["info"]["vintage"]),
                                     font=("Ubuntu", 16),
                                     bg="#1f2421",
                                     fg="#dce1de"
                                     )

        # Song Info Label Packing
        popup_song_id.grid(row=0, column=0, sticky="W")
        popup_anime_name_eng.grid(row=1, column=0, sticky="W")
        popup_anime_name_jp.grid(row=2, column=0, sticky="W")
        popup_anime_name_alt.grid(row=3, column=0, sticky="W")
        popup_anime_stats.grid(row=4, column=0, sticky="W")

    def load_current_entry_frame():
        """
        Loads current entry elements after destroying old ones
        """
        global ratio_current_entry_frame
        global user_master_dict

        ratio_current_entry_frame.destroy()
        ratio_current_entry_frame = customtkinter.CTkFrame(ratio_entries_frame, fg_color="#1f2421")
        ratio_current_entry_frame.grid(row=0, column=0, sticky="NEWS")

        if drop.get() in options:
            if (drop.get() == options[0]) or (drop.get() == options[1]):  # if user chose a certain id or generate all
                customtkinter.CTkButton(ratio_current_entry_frame,
                                        text="For Song ID " + ratio_returned_list[current_ratio_entry_index][
                                            "id"] + ":",
                                        text_color="#216869",
                                        fg_color="#1f2421",
                                        hover_color="#2F3732",
                                        font=("Ubuntu", 22),
                                        anchor="W",
                                        command=load_current_song_info
                                        ).grid(
                    row=0,
                    column=0,
                    sticky="W",
                    pady=10)
                tk.Label(ratio_current_entry_frame,
                         text="Anime Name: " + user_master_dict
                         [ratio_returned_list
                             [current_ratio_entry_index]
                             ["id"]]["info"]["animeNames"]["english"],
                         fg="#dce1de",
                         bg="#1f2421",
                         font=("Ubuntu", 12)
                         ).grid(row=1, column=0, sticky="W")
            else:
                tk.Label(ratio_current_entry_frame,
                         text="For Anime " + AMQFolderReader.id_to_name(
                             AMQDict=user_master_dict,
                             song_id=ratio_returned_list[current_ratio_entry_index]["id"]) + ":",
                         fg="#dce1de",
                         bg="#1f2421",
                         font=("Ubuntu", 18)
                         ).grid(row=0, column=0, sticky="W", pady=10)
                tk.Label(ratio_current_entry_frame,
                         text="Song ID " + ratio_returned_list[current_ratio_entry_index]["id"],
                         fg="#dce1de",
                         bg="#1f2421",
                         font=("Ubuntu", 15)
                         ).grid(
                    row=1,
                    column=0,
                    sticky="W")
            tk.Label(
                ratio_current_entry_frame,
                text="Song: " + user_master_dict[ratio_returned_list[current_ratio_entry_index]["id"]]["info"][
                    "songName"],
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 12)
            ).grid(row=2, column=0, sticky="W")
            tk.Label(
                ratio_current_entry_frame,
                text="Artist: " + user_master_dict[ratio_returned_list[current_ratio_entry_index]["id"]]["info"][
                    "artist"],
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 12)
            ).grid(row=3, column=0, sticky="W")
            tk.Label(
                ratio_current_entry_frame,
                text="Ratio: " + str(ratio_returned_list[current_ratio_entry_index]["ratio"]),
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 17)
            ).grid(row=4, column=0, sticky="SW")
            tk.Label(
                ratio_current_entry_frame,
                text="  Total Entries: " + str(ratio_returned_list[current_ratio_entry_index]["total"]),
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 14)
            ).grid(row=5, column=0, sticky="W")
            tk.Label(
                ratio_current_entry_frame,
                text="     Correct Entries: " + str(ratio_returned_list[current_ratio_entry_index]["correct"]),
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 12)
            ).grid(row=6, column=0, sticky="W")
            tk.Label(
                ratio_current_entry_frame,
                text="     Incorrect Entries: " + str(ratio_returned_list[current_ratio_entry_index]["incorrect"]),
                fg="#dce1de",
                bg="#1f2421",
                font=("Ubuntu", 12)
            ).grid(row=7, column=0, sticky="W")
        else:
            print("uh oh (approx line 400)")

    def ratio_return_function():
        """
        Destroys the master ration frame and loads a frame of the main menu
        """
        ratio_master_frame.destroy()
        main_menu_frame_load()

    ratio_back_button = customtkinter.CTkButton(ratio_master_frame,
                                                text="return",
                                                fg_color=bg,
                                                hover_color=bg,
                                                font=("Lemon/Milk", 18),
                                                text_color="#216869",
                                                width=50,
                                                command=ratio_return_function)
    ratio_back_button.grid(row=6, column=1, columnspan=2, pady=8)


# Display root
main_menu_frame_load()
root.mainloop()
