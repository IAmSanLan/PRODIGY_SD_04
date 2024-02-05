class SudokuSolver:
    def solve_sudoku(self, board):
        if not self.is_valid_board(board):
            raise ValueError("Invalid Sudoku board")

        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True  # Puzzle solved

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True  # Solution found

                board[row][col] = 0  # Backtrack

        return False  # No solution found

    def is_valid_board(self, board):
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False
        return True

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid_move(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def print_board(self, board):
        for row in board:
            print(" ".join(map(str, row)))

def main():
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [1, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solver = SudokuSolver()
    print("Unsolved Sudoku Puzzle:")
    solver.print_board(sudoku_board)

    if solver.solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Puzzle:")
        solver.print_board(sudoku_board)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
