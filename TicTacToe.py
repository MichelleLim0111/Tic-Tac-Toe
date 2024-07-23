import random

ResponseList = ["YES", "SURE", "OK", "yes", "sure", "ok", "Yes"]
ResponseList2 = ["no", "nah", "nope", "NO", "NOPE", "NAH", "No"]
boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
HUMAN = 'X'
COMPUTER = '0'
first_player = HUMAN
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

# Formatting for log_file
Heading = "Move Count  |  Player  |  Piece  |  Row  |  Column  "
Line_zero = "0                H          X"
file = open("logfile_21050349.txt", 'w')
file.write("\n" + Heading + "\n")
file.write(Line_zero)


def print_board(initial=False):
    # Print the board of the game
    print(('''
       |     |
    {}  |  {}  | {}
       |     |
    _____________
       |     |
    {}  |  {}  | {}
       |     |
    _____________
       |     |
    {}  |  {}  | {}
       |     | 
            ''').format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):
    # Loop to get suitable user input

    global row, column
    while True:
        if player is COMPUTER:
            box = get_computer_move()
            # To get the row and column for each input
            value = box + 1
            if value == 1:
                column = 1
                row = 1
            elif value == 2:
                column = 2
                row = 1
            elif value == 3:
                column = 3
                row = 1
            elif value == 4:
                column = 1
                row = 2
            elif value == 5:
                column = 2
                row = 2
            elif value == 6:
                column = 3
                row = 2
            elif value == 7:
                column = 1
                row = 3
            elif value == 8:
                column = 2
                row = 3
            elif value == 9:
                column = 3
                row = 3
            # Formatting for log file
            Column_Message = str(column)
            Row_Message = str(row)
            file.write("        " + Row_Message + "         " + Column_Message)

        else:
            box = int(input("Enter a number from 1-9 to select a box: "))
            # To get column and row for each input
            if box == 1:
                column = 1
                row = 1
            elif box == 2:
                column = 2
                row = 1
            elif box == 3:
                column = 3
                row = 1
            elif box == 4:
                column = 1
                row = 2
            elif box == 5:
                column = 2
                row = 2
            elif box == 6:
                column = 3
                row = 2
            elif box == 7:
                column = 1
                row = 3
            elif box == 8:
                column = 2
                row = 3
            elif box == 9:
                column = 3
                row = 3
            # Formatting for log file
            Column_Message = str(column)
            Row_Message = str(row)
            file.write("        " + Row_Message + "         " + Column_Message)

            try:
                box = int(box) - 1  # subtract 1 to sync with boxes[] index number


            except ValueError:
                # When user input a value that's not an integer
                print("That's not a valid number, try again.\n")
                continue

        if box < 0 or box > 8:
            print("That number is out of range,have you not played tic tac toe before? Please try again.\n")
            continue

        if boxes[box] == ' ':  # initial value
            boxes[box] = player  # set to value of current player
            break
        else:
            print("Hey! That spot is taken! Try again.\n")


def get_computer_move():
    # generate computer's move randomly
    return random.randint(0, 8)


def switch_player(turn):
    # Alternate between computer and player turn depending on odd or even number
    current_player = COMPUTER if turn % 2 == 0 else HUMAN
    return current_player


def check_for_win(player, turn):
    # Check for a win or a tie using winning combinations and automatically go for a tie if all
    # box are filled without a winner
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'


def play(player, turn):
    # Loop the game until someone wins or it ends in a tie
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print("Game over. You win!\n")
            print("You won this round, but the next match will be mine! ")
            break
        elif result == 'tie':
            print("Game over. Its a tie.\n")
            print("What a shame, I guess we are all losers here.")
            break
        turn += 1
        player = switch_player(turn)
        # Formating for log file
        turn_message = "\n" + str(turn-1)
        if turn % 2 == 0:
            Player = str("C")
            Piece = str("0")
        else:
            Player = str("H")
            Piece = str("X")
        Player_message = Player
        Piece_Message = Piece
        file.write("           " + turn_message + "                " + Player_message +
                     "          " + Piece_Message)


# Begin the game:
print("Hello! Welcome to a simple game of tic-tac-toe. :D")
Response1 = input("Would you like to play? ")
Ask_again = True

while Ask_again == True:
    if any(word in Response1 for word in ResponseList):
        print("Great! I'll be your opponent for this match. :)")
        print("Go ahead, make the first move. >:D")
        print_board(initial=True)
        play(first_player, turn)
        Ask_again = False

    elif any(word in Response1 for word in ResponseList2):
        print("I WILL NOT TAKE NO FOR AN ANSWER")
        print("LETS PLAY")
        print("MAKE THE FIRST MOVE")
        print_board(initial=True)
        play(first_player, turn)
        Ask_again = False

    else:
        print("Sorry I dont understand that, can you try again?")
        Response1 = input("Would you like to play? ")
        Ask_again = True
