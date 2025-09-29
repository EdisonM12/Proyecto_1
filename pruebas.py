from rich.console import Console
console = Console()

while True:
    console.print("\n=== MENÚ ===", style="bold blue")
    console.print("1. Opción 1", style="green")
    console.print("2. Opción 2", style="yellow")
    console.print("3. Salir", style="red")

    opcion = input("Seleccione una opción:"
                   " ")
    if opcion == "1":
        console.print("Elegiste Opción 1", style="green")
    elif opcion == "2":
        console.print("Elegiste Opción 2", style="yellow")
    elif opcion == "3":
        console.print("Saliendo...", style="red")
        break
    else:
        console.print("Opción inválida", style="bold red")
