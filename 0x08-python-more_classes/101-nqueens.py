#!/usr/bin/python3
"""
N queens puzzle challenge
"""


import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the specified position.

    Args:
        board (list): The current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """
    Recursively solve the N queens problem.

    Args:
        board (list): The current state of the board.
        row (int): The current row being processed.
        N (int): The size of the board.
    """
    if row == N:
        print_solution(board)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def print_solution(board):
    """
    Print the solution of the N queens problem.

    Args:
        board (list): The final state of the board.
    """
    for i in range(len(board)):
        print(f'[{i}, {board[i]}]', end=' ')
    print()


def main():
    """
    Main function to handle command line arguments and start solving the problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(2)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(2)
    except ValueError:
        print("N must be a number")
        sys.exit(2)

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
