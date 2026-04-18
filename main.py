from rich.console import Console
from models import City, BuildingType
from ui import render_map, render_help, console

BUILD_TYPES = {
    "residencia": BuildingType.RESIDENCE,
    "rua":        BuildingType.STREET,
}

def handle_command(city: City, command: str) -> bool:
    """Processa um comando. Retorna False se o jogo deve encerrar."""
    parts = command.strip().lower().split()

    if not parts:
        return True

    if parts[0] == "sair":
        console.print("[dim]Encerrando o jogo. Até logo![/]")
        return False

    if parts[0] == "ajuda":
        render_help()
        return True

    if parts[0] == "construir":
        if len(parts) != 4:
            console.print("[red]Uso: construir x y tipo[/]")
            return True
        try:
            x, y = int(parts[1]), int(parts[2])
        except ValueError:
            console.print("[red]x e y precisam ser números inteiros.[/]")
            return True
        tipo = parts[3]
        if tipo not in BUILD_TYPES:
            console.print(f"[red]Tipo inválido. Use: {', '.join(BUILD_TYPES)}[/]")
            return True
        msg = city.build(x, y, BUILD_TYPES[tipo])
        console.print(msg)
        return True

    console.print(f"[red]Comando desconhecido: '{parts[0]}'. Digite 'ajuda' para ver os comandos.[/]")
    return True


def run():
    city = City(
        name="Nova Bahia",
        total_amount=1000,
        population_quantity=10,
        food_quantity=50,
    )

    render_map(city)

    while True:
        console.print()
        command = console.input("[bold]>[/] ")
        render_map(city)
        if not handle_command(city, command):
            break
        render_map(city)


if __name__ == "__main__":
    run()