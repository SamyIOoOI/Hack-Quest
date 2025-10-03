from rich import print
from rich.console import Console
import os
import time
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
hacked_office = False
def hacking_screen():
    console.print("[bold green]Attempting to breach system...")
    time.sleep(1.5)
    console.print("[red]Attempt failed, switching to network sabotage...")
    time.sleep(1.5)
    console.print("[bold yellow]Target network identified...Injecting jammers..")
    time.sleep(1.5)
    console.print("[bold red]Jammers detected, targetting network nodes...")
    time.sleep(1.5)
    console.print("[bold green]Network nodes down, system breach successful!")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def prompt():
    clear()
    console.print("You can access the map here: [underline blue]https://github.com/SamyIOoOI/Hack-Quest/blob/main/Map.png[/underline blue]")
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
    global current_room, Coins, inventory, stolen_atm, hacked_camera, hacked_office, hacked_database, hacked_archive
    msg = ''
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
        if 'Buy Item' in map_rooms[current_room]:
            shop_item = map_rooms[current_room]['Buy Item']
            console.print(f"[bold cyan]You can buy [bold yellow]{shop_item.title()}[bold cyan] here. Type 'buy {shop_item}' to purchase it.")
        if 'Hackable' in map_rooms[current_room]:
            hackable_device = map_rooms[current_room]['Hackable']
            console.print(f"[bold magenta]You can attempt to hack the [bold yellow]{hackable_device.title()}[bold magenta] here. Type 'hack {hackable_device}' to try.")
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
            room_data = map_rooms[current_room]
            room_item = room_data.get('Item', None)
            if room_item and item.lower() == room_item.lower() and room_item not in inventory:
                inventory.append(room_item)
                msg = f"You snatched the {room_item}."
                del map_rooms[current_room]['Item']
                if {room_item} == {'Lost Wallet'}:
                    Coins = Coins + 500
                    msg += " You found $500 in the wallet!"
                elif {room_item} == {'Tip Jar'}:
                    Coins = Coins + 350
                    msg += " You found $350 in the tip jar!"
            elif not room_item:
                msg = "There is no item to pick up here."
            elif room_item in inventory:
                msg = f"You already picked up the {room_item}."
            else:
                msg = "There is no such item here."
        if action == 'Buy':
            if 'Buy Item' in map_rooms[current_room]:
                shop_item = map_rooms[current_room]['Buy Item']
                shop_item_title = shop_item.title()
                if item.lower() == shop_item.lower():
                    if shop_item_title == 'New Laptop':
                        price = 1000
                    else:
                        price = 500
                    if Coins >= price:
                        if shop_item_title not in inventory:
                            inventory.append(shop_item_title)
                            Coins -= price
                            msg = f"You bought the {shop_item_title} for ${price}."
                        else:
                            msg = f"You already own the {shop_item_title}."
                    else:
                        msg = f"You don't have enough coins to buy the {shop_item_title}."
                else:
                    msg = f"You can't buy that here."
            else:
                msg = "There is nothing to buy here."
        if action == 'Hack':
            if 'Hackable' in map_rooms[current_room]:
                hackable_device = map_rooms[current_room]['Hackable']
                device = hackable_device.strip().lower()
                if device == 'atm cash' and not stolen_atm:
                    if any(lap in [item.lower() for item in inventory] for lap in ['old laptop', 'new laptop']):
                        hacking_screen()
                        Coins += 250
                        msg = "You have successfully hacked the ATM and withdrawn $250!"
                        stolen_atm = True
                        map_rooms['ATM'].pop('Hackable')
                    else:
                        msg = "You need a laptop to hack the ATM. Try searching the HQ for an old laptop or buy a new one from the Shopping Center!"
                else:
                    if current_room not in ['ATM', 'The HQ', 'Main Street', 'Internet Cafe', 'Shopping Center', 'Apartment', 'East Street']:
                        if 'Hacking USB' not in inventory:
                            msg = "You need the Hacking USB to hack anything in the bank!"
                            continue
                    if device == 'camera system' and not hacked_camera:
                        if 'Bank Disguise' in inventory:
                            hacking_screen()
                            msg = "You have successfully hacked the bank's camera system. You can now move freely without being caught."
                            hacked_camera = True
                            map_rooms['Bank Entrance'].pop('Hackable')
                        else:
                            msg = "You need the bank disguise from the apartment to do actions inside the bank."
                    elif device == 'archive database' and not hacked_archive:
                        if hacked_camera:
                            if any(lap in [item.lower() for item in inventory] for lap in ['new laptop']):
                                hacking_screen()
                                msg = 'You have successfully hacked into the bank archives and found the codes. You now need to hack the bank servers.'
                                hacked_archive = True
                                map_rooms['Bank Archives Room'].pop('Hackable')
                            else:
                                msg = "You need a better laptop to hack the bank systems. Try buying one from the shopping center."
                        else:
                            msg = "You need to hack the cameras first."
                    elif device == 'bank servers' and not hacked_database:
                        if hacked_archive:
                            hacking_screen()
                            msg = "You have successfully hacked into the bank servers and found the manager's PC digits. Proceed to the office area and hack the vault's security system blueprint and passcode."
                            hacked_database = True
                            map_rooms['Bank Server Room'].pop('Hackable')
                        else:
                            msg = "You need to hack the bank archives first."
                    elif device == "manager's pc" and hacked_database and not hacked_office:
                        hacking_screen()
                        msg = "You have successfully hacked into the manager's PC and found the vault's security system blueprint and passcode. Proceed to the vault and hack the protection system."
                        hacked_office = True
                        map_rooms['Bank Office Room'].pop('Hackable')
                    elif device == 'vault protection system' and hacked_office:
                        hacking_screen()
                        msg = "You have successfully hacked into the bank's vault protection system. The cash is yours!\nThank you for playing Hack Quest!"
                        Coins += 1000000
                    else:
                        msg = "You can't hack this system right now."
                    if Coins >= 1000000:
                        console.print("[bold purple] You have successfully hacked into the bank's vault protection system. The cash is yours!\n[bold magenta] Congratulations, you have completed Hack Quest and earned $1,000,000!\n[bold green]Thank you for playing Hack Quest!")
                        break
            else:
                msg = "There is nothing to hack here."
map_rooms = { 'The HQ' : {'East' : 'Main Street', 'Item': 'Old Laptop'},
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
             'Vault' : {'West' : 'Bank Office Room', 'Hackable' : 'vault Protection System'} }
clear()
prompt()
