def is_safe(board, row, col, N):
    for i in range(col):

        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):

        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):

        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N, solutions):
    if col == N:
        solutions.append([row[:] for row in board])

        return

    for i in range(N):

        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_n_queens_util(board, col + 1, N, solutions)

            board[i][col] = 0


def print_all_solutions(N):
    board = [[0] * N for _ in range(N)]

    solutions = []

    solve_n_queens_util(board, 0, N, solutions)

    if not solutions:

        print("No solution exists")

    else:

        print("Total number of solutions:", len(solutions))

        print("One of the solutions:")

        for row in solutions[0]:
            print(" ".join(map(str, row)))


def solve_n_queens():
    N = int(input("Enter the size of the chessboard (N): "))

    print_all_solutions(N)


solve_n_queens()

