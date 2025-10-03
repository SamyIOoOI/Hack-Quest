from rich import print
from rich.console import Console
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
clear()
console.print("[bold green]Hack Quest\n[bold green]----------------------\n[green]Cracking codes like 1998.\n[green italic]by Samy Mohamed")