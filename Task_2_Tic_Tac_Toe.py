board = [" "] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("---+---+---")
    print()

def winner():
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return "Draw" if " " not in board else None

def moves():
    return [i for i,x in enumerate(board) if x == " "]

def minimax(ai):
    result = winner()
    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    scores = []
    for move in moves():
        board[move] = "O" if ai else "X"
        scores.append(minimax(not ai))
        board[move] = " "
    return max(scores) if ai else min(scores)

def ai_move():
    best_score, best_move = -float("inf"), None
    for move in moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score, best_move = score, move
    board[best_move] = "O"

print("=== Tic-Tac-Toe AI ===")
print("You are X. AI is O.")
while True:
    display_board()
    try:
        pos = int(input("Choose a position (1-9): ")) - 1
        if pos not in range(9) or board[pos] != " ":
            print("Invalid position.")
            continue
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    board[pos] = "X"
    result = winner()
    if result:
        display_board()
        print("Congratulations! You won!" if result == "X" else "It's a draw!")
        break

    print("AI's move...")
    ai_move()
    result = winner()
    if result:
        display_board()
        print("AI wins! Better luck next time." if result == "O" else "It's a draw!")
        break
