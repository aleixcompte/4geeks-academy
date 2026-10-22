current_player = "X"
stop = False

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]


def play(position):
    global current_player, stop

    if position < 0 or position > 8:
        print("Posición no válida")
        return

    if board[position] != "-":
        print("Esta posición ya está ocupada")
        return

    board[position] = current_player

    print_board()

    if check_for_winner():
        print(f"¡El jugador {current_player} ha ganado!")
        stop = True
        return

    if "-" not in board:
        print("¡Empate!")
        stop = True
        return

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_for_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in winning_combinations:
        if board[a] != "-" and board[a] == board[b] == board[c]:
            return True

    return False


def new_game():
    global board, current_player, stop

    board = ["-"] * 9
    current_player = "X"
    stop = False

    print("Nueva partida")
    print_board()


def print_board():
    print(f"""
    Current board ({current_player} turn):

    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)


print("Bienvenido a TicTacToe")
print("Comandos: play 0-8, new, board, stop")
print_board()

while stop == False:
    command = input("What do you want?: ").strip()

    if command == "stop":
        stop = True

    elif command == "new":
        new_game()

    elif command == "board":
        print_board()

    elif command.startswith("play "):
        try:
            position = int(command.split()[1])
            play(position)
        except (ValueError, IndexError):
            print("Introduce una posición válida entre 0 y 8")

    else:
        print("Comando no válido")
