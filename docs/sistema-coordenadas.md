O objetivo desta etapa é criar um mecanismo de input que aceite coordenadas (como "2,3") e atualize o estado da sua cidade.

Para concluir este passo:

    Ter um dicionário de construções {'R': 'Residência'}. Uma residência deve ter 1x1 de tamanho no mapa.

    O programa irá rodar em loop que só para quando você digitar "sair".

    Permitir que o jogador escolha qual caractere colocar e onde.

1. Representação Interna vs. Visual

    A Matriz: Uma lista de listas (grid) que armazena objetos ou referências.

    Antes de colocar a construção, o jogo precisa validar se aquela coordenada existe (ex: você não pode construir em 10,10 se o seu mapa for 5x5).

2. O Fluxo de Comando (Input Parsing)

Solicitar o input: comando = input("O que deseja fazer? (ex: construir 2 3): ")

Dividir a string: partes = comando.split()

Validar:

    A primeira palavra é "construir"?

    As próximas duas são números inteiros?

    Esses números estão dentro do limite do mapa?

    O espaço já está ocupado?

4. O Ciclo de Feedback

Após o jogador digitar a coordenada e você atualizar a matriz, o jogo deve:

    Limpar a tela (para não ficar acumulando texto).

    Renderizar o mapa novamente (agora com o caractere da construção no lugar certo).

    Exibir uma mensagem de confirmação ou erro.

## Estrutura de Dados

O mapa da cidade terá o tamanho 10x10 e inicia preenchido por grama.
O mapa poderá conter construções. Há diferentes tipos de construções.
Residência é uma construção com tamanho 1x1.
Rua é uma construção com tamanho 1x1

## Comandos para o usuário interagir com a cidade

construir. Recebe 3 parametros: posição x, posição y, tipo de construção.
ajuda. Mostra os comandos disponíveis e seus respectivos parâmetros.
sair. Encerra o jogo.

## UI

Usar o símbolo pipe (|) para separar as posições no mapa. 
O mapa deve mostrar para cada linha e coluna seu numero correspondente para ajudar o usuario a se situar das posições. Além de também indicar qual é a dimensão x e qual é a dimensão y.
Deve haver um painel superior (acima do mapa) que mostre o nome da cidade. Um painel inferior (abaixo do mapa) para que o usuario digite os comandos. Coloque diversos hífens (-) para separar estas seções do mapa.

Exemplo de cidade no terminal

ESTADO DA CIDADE: SÃO PAULO 2.0 | Turno: 14 
----------------------------------------------------------------------
[ DINHEIRO: $1,250 ]  [ POPULAÇÃO: 45 ]  [ ENERGIA: 80% ]  [ COMIDA: 12 ]
----------------------------------------------------------------------

      0   1   2   3   4   5   6   7   8   9  (X)
    +---+---+---+---+---+---+---+---+---+---+
 0  | . | . | . | ~ | ~ | . | . | . | . | . |
 1  | . | H | . | ~ | ~ | . | P | . | . | . |
 2  | . | H | . | = | = | = | = | = | = | . |  <-- (Rio e Estrada)
 3  | . | . | . | ~ | ~ | . | . | I | . | . |
 4  | . | . | . | ~ | ~ | . | . | . | . | . |
(Y)

LEGENDA:
[ . ] Grama     [ H ] Residência   [ I ] Indústria
[ ~ ] Água      [ = ] Estrada      [ P ] Parque

COMANDOS:
> construir [tipo] [x] [y] | passar turno | sair
----------------------------------------------------------------------
Próximo comando: _
