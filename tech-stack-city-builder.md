# Tech Stack: Simulador de Cidade em Terminal (Python)
1. Linguagem e Ambiente

    Linguagem: Python 3.10+ (recomenda-se versões recentes para o uso de Type Hinting, que ajuda muito na manutenção de sistemas complexos).

    Gerenciador de Pacotes: pip ou poetry.

    Ambiente Virtual: venv ou conda.

2. Bibliotecas de Interface (TUI - Terminal User Interface)

Para um jogo de gerenciamento, você precisa de uma forma de desenhar o mapa e os menus sem que a tela "pisque" (o que acontece se você usar apenas print).

    Opção A (Recomendada - Moderna): Rich

        Por que: Excelente para formatar tabelas (painéis de recursos), renderizar cores (ANSI), barras de progresso (construção) e até "markdown" para manuais.

    Opção B (Para Dashboards Complexos): Textual

        Por que: Criada pelos mesmos autores da Rich, ela permite criar interfaces com eventos, botões e grids quase como se fosse CSS/HTML, mas tudo no terminal. É ideal para city builders com muitos menus.

    Opção C (Baixo Nível/Movimentação): Blessed

        Por que: Se você quiser que o jogador use as setas do teclado para mover um cursor pelo mapa da cidade, a blessed facilita a detecção de teclas e o posicionamento do cursor em coordenadas (x, y).

3. Estrutura de Dados e Lógica

    NumPy (Opcional, mas útil): Se o seu mapa for muito grande (ex: 100x100), o NumPy lida com matrizes de forma muito performática.

    Pydantic ou Dataclasses: Para definir as entidades do jogo (Ex: Building, Citizen, Resource) com validação de dados.

4. Arquitetura do Software (Conceitos Chave)

Um city builder é essencialmente uma máquina de estados.

    O Loop Principal (Game Loop): Um while True que processa entradas, atualiza a simulação econômica e redesenha a tela.

    Tick System: O tempo não passa por "frame", mas por "ticks". Ex: a cada 1 segundo, ocorre um "tick" de produção de impostos.

    Sistema de Coordenadas: Uma matriz 2D (lista de listas) onde cada célula armazena um objeto ou um ID de construção.

Exemplo de Estrutura de Classes

Para ajudar no seu início com o Claude/Cursor, aqui está uma sugestão de como organizar as classes:

```python
from dataclasses import dataclass

@dataclass
class Building:
    name: str
    char: str      # Caractere que aparecerá no mapa (ex: 'H' para House)
    cost: int
    upkeep: int    # Custo de manutenção por turno
    population_capacity: int

class CityMap:
    def __init__(self, width, height):
        self.grid = [[" " for _ in range(width)] for _ in range(height)]

    def place_building(self, x, y, building: Building):
        self.grid[y][x] = building.char
```

## Plano de Estudo e Primeiros Passos

    Semana 1: Instale a biblioteca Rich e aprenda a imprimir uma "tabela" que represente o status da cidade (Dinheiro, População, Comida).

    Semana 2: Implemente o sistema de coordenadas básico onde você pode "construir" algo digitando coordenadas.

    Semana 3: Crie o Game Loop onde o dinheiro aumenta ou diminui automaticamente com o passar do tempo.