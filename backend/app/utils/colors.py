
#* Define Colored-print (for debugging)

from typing import Any
from rich.console import Console

console = Console()

def pred(text: Any) -> None: console.print(f"[bold red]{str(text)}[/bold red]")

def pgreen(text: Any) -> None: console.print(f"[bold green]{str(text)}[/bold green]")

def pblue(text: Any) -> None: console.print(f"[bold blue]{str(text)}[/bold blue]")

def pyellow(text: Any) -> None: console.print(f"[bold yellow]{str(text)}[/bold yellow]")

def pmagenta(text: Any) -> None: console.print(f"[bold magenta]{str(text)}[/bold magenta]")

def pcyan(text: Any) -> None: console.print(f"[bold cyan]{str(text)}[/bold cyan]")
