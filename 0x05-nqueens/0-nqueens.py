#!/usr/bin/python3
"""This module define q program that solves the N-Queens puzzle
"""
import sys


def solve_n_queens_all(N):
    def is_safe(board, row, col, N):
        for i in range(col):
            if board[row][i] == 1:
                return False
            for j in range(N):
                check = (row - j == col - i or row - j == i - col)
                if (board[j][i] == 1 and check):
                    return False
        return True

    def solve_n_queens_util(board, col, N, solutions):
        if col >= N:
            temp = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        temp.append([i, j])
            solutions.append(temp)
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_n_queens_util(board, col + 1, N, solutions)
                board[i][col] = 0

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    _, N = sys.argv

    try:
        N = int(N)
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_n_queens_all(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
