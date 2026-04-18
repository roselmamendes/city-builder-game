from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from models import City, BuildingType

console = Console()

SYMBOLS = {
    None:                  " . ",
    BuildingType.RESIDENCE: " C ",
    BuildingType.STREET:    " = ",
}

def render_map(city: City) -> None:
    # city header
    console.print(Panel(f"[bold cyan]🏙️  {city.name}[/]", box=box.HORIZONTALS))

    # status
    console.print(
        f"  💰 [green]${city.total_amount}[/]   "
        f"👥 {city.population_quantity}   "
        f"🌾 {city.food_quantity}"
    )
    console.print()

    # x axis label
    header = "      " + "".join(f"  {x:<2}" for x in range(city.grid_size))
    console.print(f"[dim]{header}[/]")
    console.print(f"[dim]   X →[/]")

    # map rows
    for y, row in enumerate(city.grid):
        cells = "|".join(SYMBOLS[cell.building_type if cell else None] for cell in row)
        y_label = f"[dim]Y {y:>2}[/]"
        console.print(f"{y_label}  |{cells}|")

    # bottom separator
    console.print()
    console.print("-" * 55)

def render_help() -> None:
    table = Table(box=box.SIMPLE, header_style="bold cyan", title="Comandos disponíveis")
    table.add_column("Comando",    style="bold")
    table.add_column("Parâmetros")
    table.add_column("Descrição")

    table.add_row("construir", "x  y  tipo", "Constrói na posição (x, y)")
    table.add_row("",          "",           "[dim]tipos: residencia | rua[/]")
    table.add_row("ajuda",     "",           "Mostra esta tela")
    table.add_row("sair",      "",           "Encerra o jogo")

    console.print(table)