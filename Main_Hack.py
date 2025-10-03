from rich import print
from rich.console import Console
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
console = Console()
current_room = 'The HQ'
Coins = 0
vowel_var = ['a', 'e', 'i', 'o', 'u']
inventory = []
def prompt():
    if not inventory:
        console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green italic]Cracking codes like 1998.\n[bold green]----------------------\n[Yellow]Inventory: Empty, Coins: {Coins}")
    if inventory:
        console.print(f"[bold green]Hack Quest\n[bold green]----------------------\n[green italic]Cracking codes like 1998.\n[bold green]----------------------\n[Yellow]Inventory: {inventory}, Coins: {Coins}") 
map_rooms = { 'The HQ' : {'East' : 'Main Street'},
             'Main Street' : {'West' : 'The HQ', 'North' : 'Internet Cafe', 'South' : 'ATM', 'East' : 'East Street'},
             'Internet Cafe' : {'South' : 'Main Street'},
             'ATM' : {'North' : 'Main Street'},
             'East Street' : {'West' : 'Main Street', 'East' : 'Bank Entrance', 'North' : 'Apartment', 'South' : 'Shopping Center'},
             'Apartment' : {'South' : 'East Street'},
             'Shopping Center' : {'North' : 'East Street'},
             'Bank Entrance' : {'West' : 'East Street', 'East' : 'Bank Office Room', 'North' : 'Bank Server Room', 'South' : 'Bank Archives Room'},
             'Bank Archives Room' : {'North' : 'Bank Entrance'},
             'Bank Server Room' : {'South' : 'Bank Entrance'},
             'Bank Office Room' : {'West' : 'Bank Entrance', 'East' : 'Vault'},
             'Vault' : {'West' : 'Bank Office Room'}}
clear()
prompt()
