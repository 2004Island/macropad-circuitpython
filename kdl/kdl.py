class kdl_interpreter():
    def __init__(self, sizes, source_file):
        """Takes in a 1D array of sizes containing the columns for a given row. The number of rows is the length
        of the list. Also takes in a path to a kdl source file to parse"""

        self.is_pressed = [[False for _ in range(i)] for i in sizes]
        self.states = []
        self.state = 0
        self.state_semaphore = False

        keywords = ["setstate"]

        with open(source_file, 'r') as file:
            # Track currently being assembled state and its number
            current_state_num = None
            current_state = [[None for _ in range(i)] for i in sizes]

            # Parse file line by line
            for line in file:
                tokens = line.split(' ')

                # If State x
                if tokens[0] == "State":
                    # Append previous state (num, state) and start on next state. 
                    if not current_state_num == None: 
                        self.states.append(current_state)
                        current_state = [[None for _ in range(i)] for i in sizes]

                    current_state_num = int(tokens[1])

                # Defining key mapping
                elif tokens[0].endswith(':') and ',' in tokens[0]:
                    row, column = tokens[0].split(',')
                    column = int(column.split(':')[0])
                    row = int(row)
                    action = tokens[1]

                    # If the action is a keyword, add it as (id, parameter), otherwise, (0, char)
                    if not action in keywords: current_state[row][column] = (0, action)
                    else: 
                        current_state[row][column] = (keywords.index(action)+1, tokens[2])
                        
            # Append final state at the end
            self.states.append( current_state)

                



    def key_pressed(self, row, column):
        """Marks a given key as pressed and returns its value"""

        # Dont get stuck in a loop switching states rapidly. Set state
        if not self.state_semaphore and self.states[self.state][row][column][0] == 1:
            self.state_semaphore = True
            self.state = int(self.states[self.state][row][column][1])

        # TODO: Out of bounds error handling. Mark pressed
        self.is_pressed[row][column] = True

        # Return none if it was an action, otherwise return key
        if not self.states[self.state][row][column][0] == 0:
            return

        return self.states[self.state][row][column][1]

    def key_released(self, row, column):
        # Release semaphor and mark key unpressed
        self.is_pressed[row][column] = False
        if self.states[self.state][row][column][0] == 1:
            self.state_semaphore = False
        return

    def is_pressed(self, row, column):
        return self.is_pressed[row][column]