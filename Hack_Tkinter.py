import os
import sys
import time
from tkinter import Button, Label, LabelFrame, Listbox, PhotoImage
from tkinter.ttk import Progressbar
import tkinter as tk
current_room = 'The HQ'
Coins = 0
vowel_var = ['a', 'e', 'i', 'o', 'u']
inventory = []
stolen_atm = False
hacked_camera = False
hacked_database = False
hacked_archive = False
hacked_office = False
hacked_value = 1
hacked_token = False
msg = ''
start_game = False
start_instructions = False
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "images", relative_path)
gui = tk.Tk()
gui.title("Hack Quest")
gui.geometry("700x450")
gui.config(bg="PeachPuff")
gui.resizable(False, False)
def check_dropdown():
    print(selected_menu.get())
prompt_variable = tk.StringVar()
menu_list = ['Start', 'Instructions']
selected_menu = tk.StringVar()
drop_down = tk.OptionMenu(gui, selected_menu, *menu_list)
drop_down.config(bg='light pink', borderwidth='1', relief='solid', width=60, height=1)
prompt_variable.set("Choose Start to start, Instructions to learn how to play or close the window to exit.")
prompt_label = tk.Label(gui, textvariable=prompt_variable, bg='light pink', font=("Arial", 12, 'bold'), borderwidth='2', wraplength=695, height=6, relief='solid')
confirm_button = tk.Button(gui, text='Confirm', height=1, width=4, relief='solid', borderwidth=2, command=check_dropdown, bg='light pink')
prompt_label.place(x=36, y=20)
drop_down.place(x=80, y=300)
confirm_button.place(x=297, y=360)
map_rooms = { 'The HQ' : {'East' : 'Main Street', 'Item': 'Old Laptop'}, ## Map Database
             'Main Street' : {'West' : 'The HQ', 'North' : 'Internet Cafe', 'South' : 'ATM', 'East' : 'East Street', 'Item': 'Lost Wallet'},
             'Internet Cafe' : {'South' : 'Main Street', 'Item' : 'Tip Jar'},
             'ATM' : {'North' : 'Main Street', 'Hackable' : 'ATM Cash'},
             'East Street' : {'West' : 'Main Street', 'East' : 'Bank Entrance', 'North' : 'Apartment', 'South' : 'Shopping Center', 'Item' : 'Hacking USB'},
             'Apartment' : {'South' : 'East Street', 'Item' : 'Bank Disguise'},
             'Shopping Center' : {'North' : 'East Street', 'Buy Item' : 'new Laptop'},
             'Bank Entrance' : {'West' : 'East Street', 'East' : 'Bank Office Room', 'North' : 'Bank Server Room', 'South' : 'Bank Archives Room', 'Hackable' : 'camera System'},
             'Bank Archives Room' : {'North' : 'Bank Entrance', 'Hackable' : 'archive Database'},
             'Bank Server Room' : {'South' : 'Bank Entrance', 'Hackable' : 'bank Servers'},
             'Bank Office Room' : {'West' : 'Bank Entrance', 'East' : 'Vault', 'Hackable' : "manager's pc"},
             'Vault' : {'West' : 'Bank Office Room', 'Hackable' : 'vault Protection System'} } ## Passwords Database
password_patterns = {'First' : {'1': '7x9kQwTz8pLk3Jv', '2':'4mN2bXcV9kQwTz', '3' : '9kQwTz5rTgH8sQw', '4' : 'QwTz7uYhLk9kQwTz3', 'Answer' : '9kQwTz'},
                     'Second' : {'1':'2pL8rXy7mNqL', '2':'5tGhLpL8rXy', '3':'8pL8rXy6vBnMp', '4':'3kLpL8rXy9', 'Answer':'pL8rXy'},
                      'Third' : {'1':'1Zx7LmN2b', '2':'3nMZx7LmN', '3':'4Zx7LmN5t', '4':'6p7Zx7LmNN', 'Answer':'Zx7LmN'},
                       'Fourth' : {'1':'tR5qLp8nM', '2':'2tR5qLp3bN', '3':'4tR5qL5vGtR5qLp', '4':'6tR5qLp7kL', 'Answer':'tR5qLp'},
                        'Fifth' : {'1':'1Qp8zLm2b3', '2':'4nMQp8zLm', '3':'5Qp8zLm6t7', '4':'8pQp8zLm9N', 'Answer':'Qp8zLm'},
                         'Sixth' : {'1':'vT3kXy1a2b', '2':'3c4vT3kXy5d', '3':'6e7f8vT3kXy', '4':'9g0h1vT3kXy2', 'Answer':'vT3kXy'} }
## Room & Item Images (must be loaded after root window is created)
def load_images():
    global hq, old_laptop, main_street, lost_wallet, internet_cafe, tip_jar, atm, atm_cash, apartment, disguise, new_laptop, usb, east_street, shopping_center, bank_entrance, cameras, server_room, servers, archive_room, archives, office_room, office, vault_room, vault
    hq = PhotoImage(file=resource_path('hq_converted.png'))
    old_laptop = PhotoImage(file=resource_path('oldlaptop_converted.png'))
    main_street = PhotoImage(file=resource_path('mainstreet_converted.png'))
    lost_wallet = PhotoImage(file=resource_path('lostwallet_converted.png'))
    internet_cafe = PhotoImage(file=resource_path('cafe_converted.png'))
    tip_jar = PhotoImage(file=resource_path('tipjar_converted.png'))
    atm = PhotoImage(file=resource_path('atm_converted.png'))
    atm_cash = PhotoImage(file=resource_path('atmcash_converted.png'))
    apartment = PhotoImage(file=resource_path('apartment_converted.png'))
    disguise = PhotoImage(file=resource_path('disguise_converted.png'))
    new_laptop = PhotoImage(file=resource_path('newlaptop_converted.png'))
    usb = PhotoImage(file=resource_path('hackingusb_converted.png'))
    east_street = PhotoImage(file=resource_path('eaststreet_converted.png'))
    shopping_center = PhotoImage(file=resource_path('shoppingcenter_converted.png'))
    bank_entrance = PhotoImage(file=resource_path('bank_converted.png'))
    cameras = PhotoImage(file=resource_path('camera.png'))
    server_room = PhotoImage(file=resource_path('bankservers_converted.png'))
    servers = PhotoImage(file=resource_path('servers.png'))
    archive_room = PhotoImage(file=resource_path('bankarchive_converted.png'))
    archives = PhotoImage(file=resource_path('archive.png'))
    office_room = PhotoImage(file=resource_path('bankoffice_converted.png'))
    office = PhotoImage(file=resource_path('office.png'))
    vault_room = PhotoImage(file=resource_path('vault_converted.png'))
    vault = PhotoImage(file=resource_path('vaultroom.png'))
load_images()
## /Room & Item Images
gui.mainloop()