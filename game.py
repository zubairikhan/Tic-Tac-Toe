from tkinter import *
from PIL import ImageTk, Image
import math
import random
from tkinter import messagebox


def isDiagDown(board, mark):
    for i in range(3):
        if board[i][i] != mark:
            return False
    return True


def isDiagUp(board, mark):
    for i in range(3):
        if board[2 - i][i] != mark:
            return False
    return True


def isVertical(board, j, mark):
    for i in range(3):
        if board[i][j] != mark:
            return False
    return True


def isHorizontal(board, i, mark):
    for j in range(3):
        if board[i][j] != mark:
            return False
    return True


def isWin(board, i, j, mark):
    if isVertical(board, j, mark):
        return True
    if isHorizontal(board, i, mark):
        return True

    if i == j or 2 - i == j:
        if isDiagUp(board, mark):
            return True
        if isDiagDown(board, mark):
            return True

    return False


def playerTurn(board, box, var):
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global markedBoxes
    
    r = box // 3
    c = box % 3 - 1
    if c==-1:
        r= r-1
        c=2

    board[r][c] = ' o '
    if box==1:
        button_1.grid_forget
        button_1= Button(frame, image=circle, state=DISABLED)
        button_1.grid(row=1,column=0)
    elif box==2:
        button_2.grid_forget
        button_2= Button(frame, image=circle, state=DISABLED)
        button_2.grid(row=1,column=1)
    elif box==3:
        button_3.grid_forget
        button_3= Button(frame, image=circle, state=DISABLED)
        button_3.grid(row=1,column=2)
    elif box==4:
        button_4.grid_forget
        button_4= Button(frame, image=circle, state=DISABLED)
        button_4.grid(row=2,column=0)
    elif box==5:
        button_5.grid_forget
        button_5= Button(frame, image=circle, state=DISABLED)
        button_5.grid(row=2,column=1)
    elif box==6:
        button_6.grid_forget
        button_6= Button(frame, image=circle, state=DISABLED)
        button_6.grid(row=2,column=2)
    elif box==7:
        button_7.grid_forget
        button_7= Button(frame, image=circle, state=DISABLED)
        button_7.grid(row=3,column=0)
    elif box==8:
        button_8.grid_forget
        button_8= Button(frame, image=circle, state=DISABLED)
        button_8.grid(row=3,column=1)
    elif box==9:
        button_9.grid_forget
        button_9= Button(frame, image=circle, state=DISABLED)
        button_9.grid(row=3,column=2)
    
    markedBoxes += 1

    if isWin(board, r, c, ' o '):
        response= messagebox.askyesno("Game over", "Human wins!\nPlay again?")
        if response==1:
            play_again()
        else:
            root.destroy()
    
    elif markedBoxes == 9:
        response= messagebox.askyesno("Game over", "It's a tie!\nPlay again?")
        if response==1:
            play_again()
        else:
            root.destroy()

    elif computerTurn(board, markedBoxes, var):
        response= messagebox.askyesno("Game over", "Computer wins\nPlay again?")
        if response==1:
            play_again()
        else:
            root.destroy()
    
    markedBoxes += 1


def computerTurn(board, depth, var):
    # selecting best turn
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    
    maxScore = - math.inf
    move_r = -1
    move_c = -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == '   ':
                board[i][j] = ' x '
                score = alphabeta(board, i, j, depth + 1, -math.inf, math.inf, False, var)
                if score > maxScore:
                    move_r = i
                    move_c = j
                    maxScore = score
                board[i][j] = '   '

    board[move_r][move_c] = ' x '

    if move_r==0 and move_c==0:
        button_1.grid_forget
        button_1= Button(frame, image=cross, state=DISABLED)
        button_1.grid(row=1,column=0)
    elif move_r==0 and move_c==1:
        button_2.grid_forget
        button_2= Button(frame, image=cross, state=DISABLED)
        button_2.grid(row=1,column=1)
    elif move_r==0 and move_c==2:
        button_3.grid_forget
        button_3= Button(frame, image=cross, state=DISABLED)
        button_3.grid(row=1,column=2)
    elif move_r==1 and move_c==0:
        button_4.grid_forget
        button_4= Button(frame, image=cross, state=DISABLED)
        button_4.grid(row=2,column=0)
    elif move_r==1 and move_c==1:
        button_5.grid_forget
        button_5= Button(frame, image=cross, state=DISABLED)
        button_5.grid(row=2,column=1)
    elif move_r==1 and move_c==2:
        button_6.grid_forget
        button_6= Button(frame, image=cross, state=DISABLED)
        button_6.grid(row=2,column=2)
    elif move_r==2 and move_c==0:
        button_7.grid_forget
        button_7= Button(frame, image=cross, state=DISABLED)
        button_7.grid(row=3,column=0)
    elif move_r==2 and move_c==1:
        button_8.grid_forget
        button_8= Button(frame, image=cross, state=DISABLED)
        button_8.grid(row=3,column=1)
    elif move_r==2 and move_c==2:
        button_9.grid_forget
        button_9= Button(frame, image=cross, state=DISABLED)
        button_9.grid(row=3,column=2)
    

    return isWin(board, move_r, move_c, ' x ')


def alphabeta(board, move_i, move_j, depth, al, be, isMax, var):
    # computer turn
    if isMax:
        if isWin(board, move_i, move_j, ' o '):
            return -20 + depth + random.choice([-1, 1]) * 3 * var
    else:
        if isWin(board, move_i, move_j, ' x '):
            return 20 - depth + random.choice([-1, 1]) * 3 * var
    if depth == 9:
        return 0

    if isMax:
        maxScore = -math.inf

        for row in range(3):
            if maxScore > be:
                break
            for col in range(3):
                if maxScore > be:
                    break
                if board[row][col] == '   ':
                    board[row][col] = ' x '
                    sc = alphabeta(board, row, col, depth + 1, maxScore, be, False, var)
                    maxScore = max(sc, maxScore)
                    board[row][col] = '   '

        return maxScore

    else:
        minScore = math.inf

        for row in range(3):
            if minScore < al:
                break
            for col in range(3):
                if minScore < al:
                    break
                if board[row][col] == '   ':
                    board[row][col] = ' o '
                    sc = alphabeta(board, row, col, depth + 1, al, minScore, True, var)
                    if sc < minScore:
                        minScore = sc

                    board[row][col] = '   '
        return minScore

def start_game(board, level):
    global var
    global label
    global button_easy
    global button_medium
    global button_impossible
    global markedBoxes
    
    markedBoxes=0

    d=int(level)

    var = (3-d)*2
    if d==3:
        diff_level= "Impossible"
    elif d==1:
        diff_level= "Medium"
    else:
        diff_level= "Easy"
    

    
    for i in range(3):
        board.append([])
        for _ in range(3):
            board[i].append('   ')


    label.grid_forget()
    button_easy.grid_forget()
    button_medium.grid_forget()
    button_impossible.grid_forget()
    
    diff_level_label= Label(frame, text="Difficulty level: " + diff_level)
    diff_level_label.grid(row=0, column=0, columnspan=3)
    button_1.grid(row=1,column=0)
    button_2.grid(row=1,column=1)
    button_3.grid(row=1,column=2)
    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)
    button_7.grid(row=3,column=0)
    button_8.grid(row=3,column=1)
    button_9.grid(row=3,column=2)

def play_again():
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global board
    
    board=[]
    for child in frame.winfo_children():
        child.grid_forget()
    
    label.grid(row=0,column=0,padx=10, pady=10)
    button_easy.grid(row=1,column=0, padx=10, pady=15)
    button_medium.grid(row=2,column=0, padx=10, pady=15)
    button_impossible.grid(row=3,column=0, padx=10, pady=15)

    button_1= Button(frame, image=plain, command= lambda: playerTurn(board,1,var))
    button_2= Button(frame, image=plain, command= lambda: playerTurn(board,2,var))
    button_3= Button(frame, image=plain, command= lambda: playerTurn(board,3,var))
    button_4= Button(frame, image=plain, command= lambda: playerTurn(board,4,var))
    button_5= Button(frame, image=plain, command= lambda: playerTurn(board,5,var))
    button_6= Button(frame, image=plain, command= lambda: playerTurn(board,6,var))
    button_7= Button(frame, image=plain, command= lambda: playerTurn(board,7,var))
    button_8= Button(frame, image=plain, command= lambda: playerTurn(board,8,var))
    button_9= Button(frame, image=plain, command= lambda: playerTurn(board,9,var))


if __name__ == '__main__':

    board=[]
    var=0
    markedBoxes=0
    
    root= Tk()
    root.title("Tic-Tac-Toe")
    root.iconbitmap("icon.ico")
    root.minsize(400,350)

    frame= LabelFrame(root,padx=20,pady=20)
    frame.pack(padx=10,pady=10)

    label=Label(frame, text="Select difficulty")

    plain= ImageTk.PhotoImage(Image.open("plain.png"))
    circle= ImageTk.PhotoImage(Image.open("O.png"))
    cross= ImageTk.PhotoImage(Image.open("X.png"))

    button_easy= Button(frame, text="Easy", width=10, command= lambda: start_game(board, 0))
    button_medium= Button(frame, text="Medium", width=10, command= lambda: start_game(board, 1))
    button_impossible= Button(frame, text="Impossible", width=10,command= lambda: start_game(board, 3))

    button_1= Button(frame, image=plain, command= lambda: playerTurn(board,1,var))
    button_2= Button(frame, image=plain, command= lambda: playerTurn(board,2,var))
    button_3= Button(frame, image=plain, command= lambda: playerTurn(board,3,var))
    button_4= Button(frame, image=plain, command= lambda: playerTurn(board,4,var))
    button_5= Button(frame, image=plain, command= lambda: playerTurn(board,5,var))
    button_6= Button(frame, image=plain, command= lambda: playerTurn(board,6,var))
    button_7= Button(frame, image=plain, command= lambda: playerTurn(board,7,var))
    button_8= Button(frame, image=plain, command= lambda: playerTurn(board,8,var))
    button_9= Button(frame, image=plain, command= lambda: playerTurn(board,9,var))


    label.grid(row=0,column=0,padx=10, pady=15)
    button_easy.grid(row=1,column=0, padx=10, pady=15)
    button_medium.grid(row=2,column=0, padx=10, pady=15)
    button_impossible.grid(row=3,column=0, padx=10, pady=15)


    root.mainloop()
