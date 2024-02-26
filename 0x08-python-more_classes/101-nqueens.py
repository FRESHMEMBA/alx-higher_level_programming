#!/usr/bin/python3
"""
N queens puzzle challenge
"""


import sys

def is_safe(board, row, col, N):
    """
    Checks if there is a queen in a row or column or diagonal
    """
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens(board, row, N):
    """
    Solves the puzzle
    """
    if row == N:
        print_solution(board)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, N)
            board[row][col] = '.'  # Backtrack

def print_solution(board):
    """
    Displays the solution
    """
    for row in board:
        print(''.join(row))
    print()

def main():
    """
    Entry point of the program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
