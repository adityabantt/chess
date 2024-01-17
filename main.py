import chess.engine
from time import sleep
import clipboard
from pyautogui import click

board = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

def show_next_step(fen):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")

    white = False
    # That blabla is the FEN of the starting position
    board = chess.Board(fen)
    for i in range(len(fen)):
        if fen[i] == " ":
            if fen[i+1] == "w":
                white = True
                break                

    result = engine.play(board, chess.engine.Limit(time=5))
    board.push(result.move)
    return result.move, white

    engine.quit()

def main():
    while True:
        sleep(1)
        click(1857, 94) # scan
        sleep(3)
        click(1852, 132) # copy fen
        sleep(0.1)
        fen = clipboard.paste()
        move, white = show_next_step(fen)
        move = str(move)

        if white == False:
            scolumn = 8 - board[move[0]] + 1
            srow = int(move[1])
            ecolumn = 8 - board[move[2]] + 1
            erow = int(move[3])
        else:
            srow = 8 - int(move[1]) + 1
            scolumn = board[move[0]]
            erow = 8 - int(move[3]) + 1
            ecolumn = board[move[2]]

        sleep(0.2)
        click(190 + ((scolumn)*121) - 60, 82 + ((srow)*121) - 60)
        sleep(0.2)
        click(190 + ((ecolumn)*121) - 60, 82 + ((erow)*121) - 60)

if __name__ == "__main__":
    main()