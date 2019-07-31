board=[" " for i in range(10)]

def insertLetter(letter, pos):
        board[pos] = letter

def spaceIsFree(pos):
        return board[pos] == " "

def printBoard(board):
        print("   |   |")
        print(" " + board[1] + " | " + board[2] + " | " + board[3])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + board[4] + " | " + board[5] + " | " + board[6])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + board[7] + " | " + board[8] + " | " + board[9])
        print("   |   |")

def isWinner(bo, le):
        return (bo[1]==bo[2]==bo[3]==le or
        bo[4]==bo[5]==bo[6]==le or
        bo[7]==bo[8]==bo[9]==le or
        bo[1]==bo[4]==bo[7]==le or
        bo[2]==bo[5]==bo[8]==le or
        bo[3]==bo[6]==bo[9]==le or
        bo[1]==bo[5]==bo[9]==le or
        bo[3]==bo[5]==bo[7]==le)

def playerMove():
        run=True
        while run:
                move=input(" Enter the number : ")
                try:
                        move=int(move)
                        if move>0 and move<10:
                                if spaceIsFree(move):
                                        run=False
                                        insertLetter('X', move)
                                else:
                                        print("space is full")
                        else:
                                print("Invalid number")
                except:
                        print("print valid number")

def compMove():
        possible_moves=[x for x, letter in enumerate(board) if letter==" " and x!=0]
        move=0
        for let in ['O', 'X']:
                for i in possible_moves:
                        boardcopy=board[:]
                        boardcopy[i]=let
                        if isWinner(boardcopy, let):
                                move=i
                                return move
        cornerOpen=[]
        for i in possible_moves:
                if i in [1,3,7,9]:
                        cornerOpen.append(i)
        if len(cornerOpen)>0:
                move=selectRandom(cornerOpen)
                return move
        if 5 in possible_moves:
                move=5
                return move
        edgesOpen=[]
        for i in possible_moves:
                if i in [2,6,8,4]:
                        edgesOpen.append(i)
        if len(edgesOpen)>0:
                move=selectRandom(edgesOpen)
        return move


def selectRandom(li):
        import random
        r=random.randrange(0, len(li))
        return li[r]

def isBoardFull(board):
        if board.count(" ")>1:
                return False
        else:
                return True

def main():
        printBoard(board)
        while(not isBoardFull(board)):
                if not(isWinner(board, 'O')):
                        playerMove()
                        printBoard(board)
                else:
                        print("Os Won")
                        break
                if not(isWinner(board, 'X')):
                        move=compMove()
                        if move==0:
                                print("Tie")
                                break
                        else:
                                insertLetter('O', move)
                                print("computer placed at ", move)
                                printBoard(board)
                else:
                        print("You Won")
                        break
        
        if isBoardFull(board):
                print("Draw")
main()