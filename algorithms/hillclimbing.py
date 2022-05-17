import random

# Class to hold chess board configuration
class NQueen:
    def __init__(self, row=None, column=None):
        self.row = row
        self.column = column

    def move(self):
        self.row += 1

    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column

    def if_conflict(self, q):
        #  Check rows, columns & diagonals
        if(self.row == q.get_row() or 
            self.column == q.get_column() or 
            (abs(self.column - q.get_column()) == abs(self.row - q.get_row()))):
            return True
        return False

class HillClimbing:
    def __init__(self, n):
        self.n = n
        self.steps_climbed_after_last_restart = 0
        self.steps_climbed = 0
        self.heuristic = 0
        self.random_restarts = 0

    # Function to generate random chess board configuration
    def generate_board(self):
        start_board = [NQueen() for i in range(self.n)]
        for i in range(self.n):
            start_board[i] = NQueen(random.randrange(0, self.n), i)
        return start_board
    
    # Function to print current board configuration
    def print_board(self, state,positions):
        temp_board = []
        for i in range(self.n):
            t = []
            for j in range(self.n):
                t.append('_')
            temp_board.append(t)
    
        for i in range(self.n):
            r = state[i].get_row()
            c = state[i].get_column()
            temp_board[r][c] = 'Q'
        for i in range(len(state)):
            print(str(temp_board[i]).replace(',', ' ').replace('\'', ''))
        print()
        position =[]
        for row in temp_board:
            for i,item in enumerate(row):
                if item =="Q":
                    position.append(i+1)
        print()
        positions.append(position)

    # Function to count no of pairs conflicting on a board
    def find_heuristic(self, state):
        heuristic = 0
        for i in range(len(state)):
            j = i + 1
            while j < len(state):
                if (state[i].if_conflict(state[j])):
                    heuristic += 1
                j += 1
        return heuristic
    
    # Function to get the next board with lower heuristic
    def next_board(self, present_board):
        next_board = [NQueen() for i in range(self.n)]
        temp_board = [NQueen() for i in range(self.n)]
        present_heuristic = best_heuristic = self.find_heuristic(present_board)
        temp_heuristic = None

        for i in range(self.n):
            # Copy present board as best board and temp board
            next_board[i] = temp_board[i] = NQueen(present_board[i].get_row(), present_board[i].get_column())

        for i in range(self.n):
            if i>0:
                temp_board[i-1] = NQueen(present_board[i-1].get_row(), present_board[i-1].get_column())
            temp_board[i] = NQueen(0, temp_board[i].get_column())

            for j in range(self.n):
                # Get the heuristic
                temp_heuristic = self.find_heuristic(temp_board)
                # Check if temp board is better than best board
                if (temp_heuristic < best_heuristic):
                    best_heuristic = temp_heuristic
                    # Copy the temp board as best board
                    for k in range(self.n):
                        next_board[k] = NQueen(temp_board[k].get_row(), temp_board[k].get_column())
                    
                # Move the queen
                if (not temp_board[i].get_row() == self.n - 1):
                    temp_board[i].move()

        # Check whether the present board and the best board found have same heuristic
        # If yes, then randomly generate new board and assign it to the best board
        if best_heuristic == present_heuristic:
            self.random_restarts += 1
            self.steps_climbed_after_last_restart = 0
            next_board = self.generate_board()
            self.heuristic = self.find_heuristic(next_board)
        else:
            self.heuristic = best_heuristic
        self.steps_climbed += 1
        self.steps_climbed_after_last_restart += 1
        return next_board


def main(n):
    #n = int(input("Enter number of queens\t"))
    positions =[]
    if n > 3:
        q = HillClimbing(n)
        present_board = q.generate_board()
        present_heuristic = q.find_heuristic(present_board)
        while not present_heuristic == 0:
            present_board = q.next_board(present_board)
            present_heuristic = q.heuristic
        q.print_board(present_board,positions)
        print("Steps climbed", q.steps_climbed)
        print("Random restarts", q.random_restarts)
        print("Steps climbed after last restart", q.steps_climbed_after_last_restart)
    else:
        print("Solution does not exist")
    return positions
if __name__ == '__main__':
    main()
