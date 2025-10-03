from rich import print
from rich.console import Console
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
clear()
console.print("[bold green]Hack Quest\n[bold green]----------------------\n[green]Cracking codes like 1998.\n[green italic]by Samy Mohamed")
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
