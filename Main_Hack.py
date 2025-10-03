from rich import print
from rich.console import Console
import os
current_room = 'The HQ'
Coins = 0
vowel_var = ['a', 'e', 'i', 'o', 'u']
inventory = []
console = Console()
last_move = ''
stolen_atm = False
hacked_camera = False
hacked_database = False
hacked_archive = False
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def prompt():
    clear()
    console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green][italic]Cracking codes like 1998.[/italic]\n[bold green]----------------------")
    a = input("Press Y to start, H for help or Q to quit: ").lower()
    if a == 'y':
        Game()
    elif a == 'h':
        clear()
        console.print("[bold green]Instructions\n[bold green]----------------------\n[green]Welcome to Hack Quest! Your objective is to hack into the bank's vault and steal the money without getting caught. You can move between rooms, collect items, and hack systems to progress. Be careful, as some actions may alert the authorities!\n\n[bold green]Commands:\n[green]- Move: Type the direction you want to go (North, South, East, West).\n- Get Item: Type 'get [item name]' to collect an item in the room.\n- Hack: Type 'hack [system name]' to attempt hacking a system.\n- Buy Item: Type 'buy [item name]' to purchase an item if you have enough coins.\n- Inventory: Type 'inventory' to check your collected items and coins.\n- Quit: Type 'q' to exit the game.\n\n[bold green]Good luck, hacker!")
        input("\nPress Enter to return to the main menu...")
        prompt()
    elif a == 'q':
        clear()
        console.print("[bold green]Thanks for playing Hack Quest! Goodbye!")
        exit()
def Game():
    global current_room, Coins, inventory, stolen_atm, hacked_camera
    while True:
        clear()
        if not inventory:
            console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green][italic]Cracking codes like 1998.[/italic]\n[bold green]----------------------\nYou are currently in {current_room}.\n[bold green]----------------------\n[bold yellow]Inventory: Empty │ Coins: {Coins}\n[bold green]----------------------\n{msg}")
        else:
            console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green][italic]Cracking codes like 1998.[/italic]\n[bold green]----------------------\nYou are currently in {current_room}.\n[bold green]----------------------\n[bold yellow]Inventory: {inventory} │ coins: {Coins}\n[bold green]----------------------\n{msg}") 
        if 'Item' in map_rooms[current_room].keys(): ## Nearby Item Detection
            nearby_item = map_rooms[current_room]["Item"]
            if nearby_item not in inventory:
                if nearby_item[0].lower() in vowel_var:
                    console.print(f"[bold green] You see an[bold yellow] {nearby_item} [bold green]here. Type 'get' to pick it up.")
                else:
                    console.print(f"[bold green] You see a [bold yellow]{nearby_item} [bold green]here. Type 'get' to pick it up.")
        if 'Vault' in map_rooms[current_room].values(): ## Final "Boss" 
            if len(inventory) == 5:
                console.print("[bold purple] You have successfully hacked into the bank's vault protection system. The cash is yours!\n[bold magneta Thank you for playing Hack Quest!")
        user_input = input("What will you do?\n")
        split_user_input = user_input.split(' ')
        action = split_user_input[0].title()
        if len(split_user_input) > 1:
            item = split_user_input[1:]
            direction = split_user_input[1].title()
            item = ' '.join(item).title()
        if action == 'Go':
            try:
                current_room = map_rooms[current_room][direction]
                msg = f"You moved to the {current_room}."
            except:
                msg = "You can't go that way."
        if action == 'Get':
            if item == map_rooms[current_room]['Item']:
                inventory.append(item)
                msg = f"You picked up the {item}."
                del map_rooms[current_room]['Item']
            else:
                msg = "There is no such item here."
        if action == 'Hack':
            if 'Hackable' in map_rooms[current_room].keys():
                hackable_device = map_rooms[current_room]['Hackable']
                if hackable_device == 'ATM Cash' and stolen_atm == False:
                                    if hackable_device == 'ATM Cash' and 'Old Laptop' in inventory or hackable_device == 'ATM Cash'and 'New Laptop' in inventory:
                                          coins = coins + 250
                                          msg = "You have sucessfully hacked the ATM and withdrawn $250!"
                                          stolen_atm = True
                elif hackable_device == 'Camera System' and hacked_camera == False:
                     if 'Bank Disguise' in inventory:
                         msg = "You have successfully hacked the bank's camera system. You can now move freely without being caught."
                         hacked_camera = True
                     else:
                          msg = "You need the bank disguise from the apartment to do actions inside the bank."
                elif hackable_device == 'Archive Database'
map_rooms = { 'The HQ' : {'East' : 'Main Street', 'Item': 'Old Laptop'},
             'Main Street' : {'West' : 'The HQ', 'North' : 'Internet Cafe', 'South' : 'ATM', 'East' : 'East Street', 'Item': 'Lost Wallet'},
             'Internet Cafe' : {'South' : 'Main Street', 'Item' : 'Tip Jar'},
             'ATM' : {'North' : 'Main Street', 'Hackable' : 'ATM Cash'},
             'East Street' : {'West' : 'Main Street', 'East' : 'Bank Entrance', 'North' : 'Apartment', 'South' : 'Shopping Center', 'Item' : 'Empty USB'},
             'Apartment' : {'South' : 'East Street', 'Item' : 'Bank Disguise'},
             'Shopping Center' : {'North' : 'East Street', 'Buy Item' : 'New Laptop'},
             'Bank Entrance' : {'West' : 'East Street', 'East' : 'Bank Office Room', 'North' : 'Bank Server Room', 'South' : 'Bank Archives Room', 'Hackable' : 'Camera System'},
             'Bank Archives Room' : {'North' : 'Bank Entrance', 'Hackable' : 'Archive Database'},
             'Bank Server Room' : {'South' : 'Bank Entrance', 'Hackable' : 'Bank Servers'},
             'Bank Office Room' : {'West' : 'Bank Entrance', 'East' : 'Vault', 'Hackable' : "Manager's pc"},
             'Vault' : {'West' : 'Bank Office Room', 'Hackable' : 'Vault Protection System'} }
clear()
prompt()
