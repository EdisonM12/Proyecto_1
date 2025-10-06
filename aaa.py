from rich.progress import Progress
from rich.align import Align
import time

def barra():
 with Progress() as progress:
    task = progress.add_task("[cyan]Procesando...", total=100)

    for i in range(100):
        progress.update(task, advance=1)
        time.sleep(0.03)

    from rich.console import Console

    console = Console()
    console.print(Align("[bold green]¡Completado![/]", align="center"))
