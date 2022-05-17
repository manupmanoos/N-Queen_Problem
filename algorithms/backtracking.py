# Function to create N x N board
def create_board(number_of_queens):
    board = []
    for i in range(0, number_of_queens):
        board.append(['_'] * number_of_queens)
    return board

# Function to print N x N board
def print_board(board,positions):
    position =[]
    for row in board:
        print(str(row).replace(',', ' ').replace('\'', ''))
        for i,item in enumerate(row):
            if item =="Q":
                position.append(i+1)
    print()
    positions.append(position)
# Function to check if two queens are conflicting each other or not
def is_safe_move(board, row, col):

    # return false if two queens share the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # return false if two queens share the same primary diagonal
    r = row
    c = col
    while r >= 0 and c < len(board):
        if board[r][c] == 'Q':
            return False
        r -= 1
        c += 1

    # return false if two queens share the same secondary diagonal
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    return True

def n_queen(board, row,positions):

    # if 'N' queens are placed successfully i.e all rows are explored, print the board
    if row == len(board):
        print_board(board,positions)
        return 

    # place queen at every column in the current row 'row' and recursively call for each valid movement
    for col in range(len(board)):

        # if no two queens threaten each other
        if is_safe_move(board, row, col):
            # place queen on the current square in board
            board[row][col] = 'Q'

            # recursively call for the next row
            n_queen(board, row + 1,positions)

            # reset the current square
            board[row][col] = '_'

def main(number_of_queens):
    #number_of_queens = int(input('Enter number of queens, N \n'))
    positions =[]
    if number_of_queens <= 3:
        print("Solution does not exist")
    else:
        board = create_board(number_of_queens)
        n_queen(board, 0,positions)
    return positions
if __name__ == '__main__':
    main()