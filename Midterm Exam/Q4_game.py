import sys
import math

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0]) #matrix size
    symbols = lines[1].split(',')
    board = []
    for i in range(2,2+n): #read board data from line 3
        row = lines[i].split(',')
        board.append(row)
    if is_valid(board, symbols, n):
        print("The board is valid")
    else:
        print("The board is invalid")
        
#Check if the board complies with all rules
def is_valid(board, symbols, n):
    #Check rows
    for i in range(n):
        if not valid_unit([board[i][j] for j in range(n)], symbols):
            return False
    #Check columns
    for j in range(n):
        if not valid_unit([board[i][j] for i in range(n)], symbols):
            return False

    sub_size = int(math.sqrt(n)) #calculate subsequent board
    for a in range(sub_size):
        for b in range(sub_size):
            sub_board = []
            for i in range(a*sub_size, (a+1)*sub_size):
                for j in range(b*sub_size, (b+1)*sub_size):
                    sub_board.append(board[i][j])
            if not valid_unit(sub_board, symbols):
                return False
    return True

def valid_unit(unit, symbols):
    new_symbols = set()
    for cell in unit:
        if cell != '.': #ignore '.'
            if cell in new_symbols:  #Symbols repeat
                return False
            if cell not in symbols:  #Check undefined symbols
                return False
            new_symbols.add(cell) #First appearance,add
    return True

#Program Entry
if __name__ == "__main__":
    main()
