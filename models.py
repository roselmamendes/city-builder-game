from dataclasses import dataclass, field
from enum import Enum

class BuildingType(Enum):
    RESIDENCE = "residence"
    STREET    = "street"

@dataclass
class Building:
    building_type: BuildingType

@dataclass
class City:
    name: str
    total_amount: int
    population_quantity: int
    food_quantity: int
    grid_size: int = 10
    grid: list = field(default_factory=list)

    def __post_init__(self):
        self.grid = [[None] * self.grid_size for _ in range(self.grid_size)]

    def build(self, x: int, y: int, building_type: BuildingType) -> str:
        if not (0 <= x < self.grid_size and 0 <= y < self.grid_size):
            return f"[red]Posição ({x},{y}) fora do mapa.[/]"
        if self.grid[y][x] is not None:
            return f"[yellow]Posição ({x},{y}) já está ocupada.[/]"
        self.grid[y][x] = Building(building_type)
        return f"[green]Construção realizada em ({x},{y}).[/]"