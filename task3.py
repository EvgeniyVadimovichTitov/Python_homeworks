# Создайте программу для игры в ""Крестики-нолики"".
from random import randint


def Print_board(board: list):
    print("-" * 13)
    for line in board:
        print("| ", end='')
        print(line[0], line[1], line[2], sep=" | ", end=" |\n")
        print("-" * 13)


def Move(char_sep: str, player: str, board: list):
    while True:
        try:
            sep_ = int(input(f'{player} каков ваш ход? '))
        except:
            print('Eror, введите число согласно полю')
            continue
        if (sep_ not in board[0]) and (sep_ not in board[1]) and (sep_ not in board[2]):
            print('Такой ход невозможен')
            continue
        else:
            for line in board:
                try:
                    line[line.index(sep_)] = char_sep
                except:
                    continue
        break


def Check_win(li: list):
    for comb in combs_win:
        if (li[comb[0][0]][comb[0][1]] ==
            li[comb[1][0]][comb[1][1]] ==
                li[comb[2][0]][comb[2][1]]):
            return False
    return True


board = [[j for j in range(i, i+3)] for i in range(1, 10, 3)]
player_1 = input('введите имя 1-го игрока: ')
player_2 = input('введите имя 2-го игрока: ')
flag = bool(randint(0, 1))
count = 0
sep_ = 'X'
play_game = True
combs_win = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2))
)
if flag:
    print(f'{player_1} ходит первым')

else:
    print(f'{player_2} ходит первым')

while play_game:
    if flag:
        Print_board(board)
        Move(sep_, player_1, board)
        flag = False
    else:
        Print_board(board)
        Move(sep_, player_2, board)
        flag = True
    count += 1
    if sep_ == 'X':
        sep_ = 'O'
    else:
        sep_ = 'X'
    if (count > 4):
        play_game = Check_win(board)
        if (count == 9):
            Print_board(board)
            play_game = False
            print('победила дружба!!!')
            continue
    if not play_game:
        Print_board(board)
        if flag:
            print(f'победил {player_2}')
        else:
            print(f'победил {player_1}')
