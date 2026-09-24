##############################################################################
############################# MINESWEEPER GAME ###############################
##############################################################################

# Make a class for the coordinates
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 0

    # Define a method to increment count 
    def add_to_count(self):
        self.count += 1

    # Define a method to check for a mine 
    def check_for_mine(self):
        if board[self.x][self.y] == "#":
            return True
        else:
            return False

    # Define a method to check the North West position
    def check_NW(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
        if self.x > 0 and self.y > 0:
            if board[self.x -1][self.y-1] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True
        
    # Define a method to check North position
    def check_N(self):
        if self.x > 0:
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
            if board[self.x -1][self.y] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the North East position
    def check_NE(self):
        if self.x > 0 and self.y < len(board[0]) - 1:
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
            if board[self.x -1][self.y+1] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the West position
    def check_W(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
         if self.y > 0:
            if board[self.x][self.y-1] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the East position
    def check_E(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
         if self.y < len(board[0]) - 1:
            if board[self.x][self.y+1] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the South West position
    def check_SW(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
         if self.x < len(board) - 1 and self.y > 0:
            if board[self.x + 1][self.y-1] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the South position
    def check_S(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
         if self.x < len(board) - 1:
            if board[self.x + 1][self.y] == "#":
                #count(self) =+ 1
                self.add_to_count()
                return True

    # Define a method to check the South East position
    def check_SE(self):
        # Check input doesn't go out of the grids bounds
        # Source used to reference logic can be found at: 
        # https://www.youtube.com/watch?v=-aFtJt1_T3k
            if self.x < len(board) - 1 and self.y < len(board[0]) - 1:
                if board[self.x + 1][self.y + 1] == "#":
                    #count(self) =+ 1
                    self.add_to_count()
                    return True


# Define function to reveal updated board
def output_reveal_board():
    for row in reveal_board:
        print("\n",row)

# Define list of board
board = [["-","-","-","-","#"],
            ["#","-","#","#","-"],
            ["#","-","#","-","#"],
            ["-","-","#","-","-"],
            ["#","#","-","#","#"]]

# Define list of board to reveal to user
reveal_board = [["?","?","?","?","?"],
                ["?","?","?","?","?"],
                ["?","?","?","?","?"],
                ["?","?","?","?","?"],
                ["?","?","?","?","?"],]

# Print welcome message
print("Welcome to Minesweeper!","\n")

# Display reveal board to user
for row in reveal_board:
    print("\n",row)
print("\n""When prompted, enter a guess for where a mine may be in the grid above!")

# Prompt user for input
while True:
    # Request user input with try except loop so that 
    # program doesn't crash upon invalid input
    try:
        x = int(input("Enter column of guess (Enter 7 to exit): "))
    except ValueError as error:
        print("Entry invalid please try again")
        continue

    # Option for user to exit program
    if x == 7: 
        break

    # Request user input with try except loop so that 
    # program doesn't crash upon invalid input
    try:
        y = int(input("Enter row of guess (Enter 7 to exit): "))
    except ValueError as error:
        print("Entry invalid please try again")

    # Option for user to exit program
    if y == 7: 
        break

    # Create instance of object
    coord = Coordinates(x,y)

    # Condition to check for mine to return mine hit
    if coord.check_for_mine() == True:
    # overwrite the reveal board 
    # print the reveal board
        reveal_board[x][y] = "#"
        print("A hit!")
        output_reveal_board()

    # Calls function to check mine positions if user entry not a hit
    else: 
        coord.check_NW()
        coord.check_N()
        coord.check_NE()
        coord.check_W()
        coord.check_E()
        coord.check_SE()
        coord.check_S()
        coord.check_SW()

    # Tells user how for choice is from mines
        print("Your choice is next to ",coord.count," mines")
        reveal_board[x][y] = coord.count

    # Print outcome of user choice
        for row in reveal_board:
            print("\n",row)


    # Exit game when user has found all mines
    if not any ("?" in row for row in reveal_board):
        break



