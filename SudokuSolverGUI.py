# SudokuSolver - Ville Martas

from tkinter import *
import time


def readyCheck(sudoku2Darray):
    # checking if the sudoku board is filled
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku2Darray[row][column] == 0:
                return False
    return True


def whatSquare(sudoku2Darray, row, column):
    # checking which sudoku square we are currently on, and returning that one
    square = []
    if row < 3:
        if column < 3:
            square = [sudoku2Darray[index][0:3] for index in range(0, 3)]
            return square
        elif column < 6:
            square = [sudoku2Darray[index][3:6] for index in range(0, 3)]
            return square
        else:
            square = [sudoku2Darray[index][6:9] for index in range(0, 3)]
            return square

    elif row < 6:
        if column < 3:
            square = [sudoku2Darray[index][0:3] for index in range(3, 6)]
            return square
        elif column < 6:
            square = [sudoku2Darray[index][3:6] for index in range(3, 6)]
            return square
        else:
            square = [sudoku2Darray[index][6:9] for index in range(3, 6)]
            return square

    else:
        if column < 3:
            square = [sudoku2Darray[index][0:3] for index in range(6, 9)]
            return square
        elif column < 6:
            square = [sudoku2Darray[index][3:6] for index in range(6, 9)]
            return square
        else:
            square = [sudoku2Darray[index][6:9] for index in range(6, 9)]
            return square


def solverFunction(root, sudoku2Darray, entries):
    # tkinter updates here so we can visualize the algorithm
    root.update()
    entries = drawGrid(sudoku2Darray, entries)
    time.sleep(0.01)

    for i in range(0, 81):
        # Finding out row and column of the current cell
        row = i//9
        column = i % 9
        if sudoku2Darray[row][column] == 0:
            for number in range(1, 10):
                # checking if number is already in the row
                if not(number in sudoku2Darray[row]):
                    # checking if number is already in the column
                    if not number in (sudoku2Darray[0][column], sudoku2Darray[1][column], sudoku2Darray[2][column], sudoku2Darray[3][column], sudoku2Darray[4][column], sudoku2Darray[5][column], sudoku2Darray[6][column], sudoku2Darray[7][column], sudoku2Darray[8][column]):
                        # checking if number is already in the "sudoku square"
                        square = whatSquare(sudoku2Darray, row, column)
                        if not number in (square[0] + square[1] + square[2]):
                            # changing cell value if everything passed
                            sudoku2Darray[row][column] = number
                            # checking if sudoku is already filled
                            if readyCheck(sudoku2Darray):
                                print("Sudoku solved.")
                                for a in range(0, 9):
                                    for b in range(0, 9):
                                        print(
                                            "[" + str(sudoku2Darray[a][b]) + "] ", end=" ")
                                    print("\n")
                                return True
                            else:
                                if solverFunction(root, sudoku2Darray, entries):
                                    return True
            break
    print("Backtracking")
    sudoku2Darray[row][column] = 0


def drawGrid(sudoku2Darray, entries):
    for i in range(0, 9):
        for j in range(0, 9):
            entries[i][j].delete(0, END)
            entries[i][j].insert(0, sudoku2Darray[i][j])
    return entries


def main():
    # initializing the sudoku to be solve
    sudoku2Darray = [[0, 0, 0, 3, 0, 0, 0, 2, 0],
                     [0, 0, 3, 2, 5, 0, 1, 0, 8],
                     [0, 0, 0, 8, 0, 0, 0, 4, 3],
                     [0, 0, 4, 0, 9, 0, 2, 0, 0],
                     [6, 8, 0, 1, 0, 2, 0, 7, 0],
                     [0, 1, 0, 7, 6, 0, 8, 0, 0],
                     [3, 4, 0, 9, 1, 5, 7, 0, 0],
                     [0, 6, 8, 4, 0, 0, 3, 1, 0],
                     [1, 9, 7, 0, 0, 0, 4, 0, 2]
                     ]
    # initializing the GUI with 9x9 cells and the solve button
    root = Tk()
    root.geometry("360x400")
    entries = [[] for i in range(0, 9)]
    for a in range(0, 360, 40):
        for b in range(0, 360, 40):
            # colouring up certain cells
            if a < 120 and b < 120 or a >= 240 and b < 120:
                temp = Entry(root, font="Helvetica 22", justify="center", width=6, disabledbackground="#1E6FBA",
                             highlightbackground="black", bg="#c0ffad", highlightcolor="red", highlightthickness=1, bd=0)
            elif a >= 240 and b >= 240 or b >= 240 and a < 120:
                temp = Entry(root, font="Helvetica 22", justify="center", width=6, disabledbackground="#1E6FBA",
                             highlightbackground="black", bg="#c0ffad", highlightcolor="red", highlightthickness=1, bd=0)
            elif a >= 120 and a < 240 and b >= 120 and b < 240:
                temp = Entry(root, font="Helvetica 22", justify="center", width=6, disabledbackground="#1E6FBA",
                             highlightbackground="black", bg="#c0ffad", highlightcolor="red", highlightthickness=1, bd=0)
            else:
                temp = Entry(root, font="Helvetica 22", justify="center", width=6, disabledbackground="#1E6FBA",
                             highlightbackground="black", highlightcolor="red", highlightthickness=1, bd=0)
            temp.place(x=a, y=b, width=40, height=40)
            index = int(b/40)
            entries[index].append(temp)

    # drawing the initial grid with the initial values
    entries = drawGrid(sudoku2Darray, entries)
    # calling the solver if "Solve!" is pressed and starting the recursive solving process
    button = Button(root, text="Solve!", bg="#000000", fg="white",  command=lambda: solverFunction(
        root, sudoku2Darray, entries))
    button.place(x=160, y=365)

    root.mainloop()


main()
