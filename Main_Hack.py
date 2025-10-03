from rich import print
from rich.console import Console
import os
current_room = 'The HQ'
Coins = 0
vowel_var = ['a', 'e', 'i', 'o', 'u']
inventory = []
console = Console()
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
    global current_room, Coins, inventory
    while True:
        clear()
        if not inventory:
            console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green][italic]Cracking codes like 1998.[/italic]\n[bold green]----------------------\nYou are currently in {current_room}.\n[bold green]----------------------\n[bold yellow]Inventory: Empty │ Coins: {Coins}")
        else:
            console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green][italic]Cracking codes like 1998.[/italic]\n[bold green]----------------------\nYou are currently in {current_room}.\n[bold green]----------------------\n[bold yellow]Inventory: {inventory} │ coins: {Coins}") 

map_rooms = { 'The HQ' : {'East' : 'Main Street', 'Item': 'Old Laptop'},
             'Main Street' : {'West' : 'The HQ', 'North' : 'Internet Cafe', 'South' : 'ATM', 'East' : 'East Street', 'Item': 'Lost Wallet'},
             'Internet Cafe' : {'South' : 'Main Street', 'Item' : 'Tip Jar'},
             'ATM' : {'North' : 'Main Street', 'Hackable' : 'Cash'},
             'East Street' : {'West' : 'Main Street', 'East' : 'Bank Entrance', 'North' : 'Apartment', 'South' : 'Shopping Center', 'Item' : 'Empty USB'},
             'Apartment' : {'South' : 'East Street', 'Item' : 'Bank Disguise'},
             'Shopping Center' : {'North' : 'East Street', 'Buy Item' : 'New Laptop'},
             'Bank Entrance' : {'West' : 'East Street', 'East' : 'Bank Office Room', 'North' : 'Bank Server Room', 'South' : 'Bank Archives Room', 'Hackable' : 'Camera System'},
             'Bank Archives Room' : {'North' : 'Bank Entrance', 'Hackable' : 'Archive Database'},
             'Bank Server Room' : {'South' : 'Bank Entrance', 'Hackable' : 'Bank Servers'},
             'Bank Office Room' : {'West' : 'Bank Entrance', 'East' : 'Vault', 'Hackable' : "Manager's pc"},
             'Vault' : {'West' : 'Bank Office Room', 'Hackable' : 'Vault Protection System'}}
clear()
prompt()
