class key():
    def __init__(self, attributes = []):
        self.color = (0,0,0)
        self.lit = False
        
        remove = []

        actions = {}

        for i in range(len(attributes)):
            action = attributes[i]
            if action[0] == "color":
                self.color = tuple(map(int,action[1:]))
                remove.append(attributes[i])
            elif action[0] == "on":
                if action[1] in ["always"]:
                    self.lit = True
            else:
                actions[action[0]] = action[1:]

        self.actions = actions

    def get_color(self): 
        return self.color

    def get_lit(self): 
        return self.lit

    def pressed(self):
        pass

    def released(self):
        pass

    def __str__(self):
        return f"Key Color:{self.color} Lit:{self.lit} Actions:{self.actions}"


class kdl_interpreter():
    def __init__(self, sizes, source_file):
        """Takes in a 1D array of sizes containing the columns for a given row. The number of rows is the length
        of the list. Also takes in a path to a kdl source file to parse"""

        self.is_pressed = [[False for _ in range(i)] for i in sizes]
        self.states = []
        self.state = 0
        self.state_semaphore = False

        keywords = ["key", "setstate", "on", "color", "press"]

        with open(source_file, 'r') as file:
            # Track currently being assembled state and its number
            current_state_num = None
            current_state = [[None for _ in range(i)] for i in sizes]

            # Parse file line by line
            for line in file:
                # Split lines by spaces, makes them lowercase and removes whitespace
                tokens = list(map( lambda x : x.strip(), list(map(lambda x : x.lower(), line.split(' ')))))

                if tokens[0] == "state":
                    if not tokens[1].isnumeric(): 
                        print(f"NOT NUMERIC: |{tokens[1]}|")
                        return

                    print(f"state: {tokens[1]}")
                    if not current_state_num == None: 
                        self.states.append(current_state)
                        current_state = [[None for _ in range(i)] for i in sizes]

                    current_state_num = int(tokens[1])
                    
                elif tokens[0] == "key":
                    if tokens[1].endswith(':') and ',' in tokens[1]:
                        # Transform x,y: to row, column tuple
                        row, column = map(int, map(lambda x : x.split(':')[0], tokens[1].split(',')))
                        print(f"{row},{column}")

                    actions = []
                    for i in range(2, len(tokens)):
                        if tokens[i] in keywords:
                            print(tokens[i])
                            actions.append([tokens[i]])
                        else:
                            actions[-1].append(tokens[i].split(',')[0])
                    
                    current_state[row][column] = key(attributes=actions)
                    print(current_state[row][column])
                '''# If State x
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
                    if action in keywords: current_state[row][column] = (keywords.index(action)+1, tokens[2])
                    else: current_state[row][column] = (0, action)
                        
            # Append final state at the end
            self.states.append( current_state)'''


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

    def is_held(self, row, column):
        return self.is_pressed[row][column]