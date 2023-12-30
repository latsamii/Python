import random

def print_board(b):
    print("Board:")
    size = len(b)
    for i in range(size):
          print((b[i]),end=" ")
    print("\n")

def main():

    board = []

    for i in range(8):
        board.append(random.randint(0,9))

    print_board(board)

    kyle_scores = 0
    class_scores = 0
    turn = 0

    while(len(board) > 0):
        print("It is player #"+str(turn % 2 + 1)+ "turn")
    

    
    
main()
