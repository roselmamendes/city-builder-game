# 🏙️ City Builder

Um jogo de construção de cidades rodando direto no terminal, feito em Python.

## Sobre o projeto

City Builder é um projeto de aprendizado desenvolvido semana a semana.  
A ideia é construir um jogo funcional no terminal onde você gerencia recursos,
constrói estruturas e acompanha o crescimento da sua cidade turno a turno.

## Tech stack

- **Python 3.10+**
- **[Rich](https://rich.readthedocs.io/en/stable/)** — interface no terminal com tabelas, painéis e cores
- **Dataclasses** — estrutura de dados da cidade e construções

## Roadmap

- [x] Semana 1 — estrutura inicial do projeto e status da cidade
- [ ] Semana 2 — sistema de coordenadas e construção de prédios
- [ ] Semana 3 — game loop com economia automática por turno

## Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/city-builder.git
cd city-builder
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Rode o jogo**
```bash
python main.py
```

## Estrutura do projeto

```
city-builder/
├── main.py          # ponto de entrada
├── requirements.txt # dependências
├── .gitignore
└── README.md
```

---

Feito com Python 🐍 e muita preguiça