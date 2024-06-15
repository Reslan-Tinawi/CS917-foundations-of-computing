class TrieNode:
    """
    Represents a node in a Trie data structure.

    Attributes:
        children (dict): A dictionary that maps characters to child TrieNodes.
        is_end_of_word (bool): Indicates whether this node represents the end of a word.
        english_word (str): The English word represented by this node (if it is the end of a word).
        morse_code (list): A list of morse code representations for the characters in the word represented by this node.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.english_word = ""
        self.morse_code = []


def build_morse_trie(dictionary: list[tuple[str, list[str]]]) -> TrieNode:
    """
    Builds a trie data structure from a dictionary of English words and their corresponding Morse code.

    Args:
        dictionary (list[tuple[str, list[str]]]): A list of tuples containing English words and their Morse code.

    Returns:
        TrieNode: The root node of the constructed trie.

    """
    root_node = TrieNode()
    for english_word, morse_code in dictionary:
        node = root_node
        for morse_code_letter in morse_code:
            if morse_code_letter not in node.children:
                node.children[morse_code_letter] = TrieNode()
            node = node.children[morse_code_letter]
        node.is_end_of_word = True
        node.english_word = english_word
        node.morse_code = morse_code
    return root_node


MORSE_CODE_TO_LETTER = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "-": "-....-",
}


def morseDecode(inputStringList: list[str]) -> str:
    """
    Decodes a list of Morse code strings into a single string.

    Args:
        inputStringList (list[str]): A list of Morse code strings.

    Returns:
        str: The decoded string.

    """
    decoded_string_list = [
        MORSE_CODE_TO_LETTER.get(inputString) for inputString in inputStringList
    ]

    decoded_string = "".join(decoded_string_list)

    return decoded_string


def morse_encode(input_str: str) -> str:
    """
    Encodes a given string into Morse code.

    Args:
        input_str (str): The string to be encoded.

    Returns:
        str: The encoded Morse code sequence.
    """
    morse_sequence = []
    for letter in input_str:
        morse_sequence.append(MORSE_CODE_DICT[letter])
    return morse_sequence


def generate_morse_strings_with_trie(morse_sequence: list[str], trie: TrieNode):
    """
    Generates a list of English words formed by translating a morse code sequence using a trie.

    Args:
        morse_sequence (list[str]): The morse code sequence to be translated.
        trie (TrieNode): The root node of the trie representing the morse code dictionary.

    Returns:
        list: A list of English words formed by translating the morse code sequence.
    """

    def backtrack(index, current_string, node):
        """
        Backtracks through the morse code sequence to find all possible English words.

        Args:
            index (int): The current index in the morse code sequence.
            current_string (str): The current string formed by translating the morse code sequence.
            node (Node): The current node in the trie representing the morse code dictionary.

        Returns:
            list: A list of English words formed by translating the morse code sequence.
        """
        if index == len(morse_sequence):
            return [node.english_word] if node.is_end_of_word else []

        current_letter = morse_sequence[index]
        result = []

        dash_letter = current_letter.replace("x", "-")
        dot_letter = current_letter.replace("x", ".")

        if dash_letter in node.children.keys():
            result.extend(
                backtrack(
                    index + 1,
                    current_string + dash_letter,
                    node.children.get(dash_letter),
                )
            )

        if dot_letter in node.children.keys():
            result.extend(
                backtrack(
                    index + 1,
                    current_string + dot_letter,
                    node.children.get(dot_letter),
                )
            )

        return result

    root_node = trie

    result = backtrack(0, "", root_node)

    return result


def morsePartialDecode(inputStringList: list[str]) -> list[str]:
    """
    This method should take a list of strings as input. Each string is equivalent to one letter
    (i.e. one morse code string). The entire list of strings represents a word.

    However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
    For example, if the word was originally TEST, then the morse code list string would normally be:
    ['-','.','...','-']

    However, with the first characters missing, I would receive:
    ['x','x','x..','x']

    With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

    We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
    When using this file, please always use the location './dictionary.txt' and place it in the same directory as
    the python script.

    This function should find and return a list of strings of all possible VALID words.
    """

    dictionaryFileLoc = "./dictionary.txt"

    # Please complete this method to perform the above described function
    def prepare_data() -> list[tuple[str, str]]:
        with open(dictionaryFileLoc) as f:
            data = f.readlines()
            data = [d.strip() for d in data]
            data = [(d.upper(), morse_encode(d.upper())) for d in data]
        return data

    # pairs of (word, morse_code)
    data = prepare_data()

    root = build_morse_trie(data)

    valid_strings = generate_morse_strings_with_trie(inputStringList, root)

    return valid_strings


class Maze:
    def __init__(self):
        """
        Constructor - You may modify this, but please do not add any extra parameters
        """
        self.coordinates_list = []
        self.min_x = 0
        self.min_y = 0
        self.grid_height = 0  # number of rows
        self.grid_width = 0  # number of columns
        self.is_adjacency_list_built = False
        self.adjacency_list = {}  # node_hash: block_type

    def addCoordinate(self, x, y, blockType):
        """
        Add information about a coordinate on the maze grid
        x is the x coordinate
        y is the y coordinate
        blockType should be 0 (for an open space) of 1 (for a wall)
        """
        # Please complete this method to perform the above described function
        self.grid_height = max(self.grid_height, x + 1)
        self.grid_width = max(self.grid_width, y + 1)
        self.coordinates_list.append((x, y, blockType))

    def node_hash_function(self, x: int, y: int) -> int:
        """
        Calculates the hash value for a given node in the grid.

        Parameters:
        - x (int): The x-coordinate of the node.
        - y (int): The y-coordinate of the node.

        Returns:
        - int: The hash value of the node.
        """
        return x * self.grid_width + y

    def node_inverse_hash_function(self, node_hash_value: int) -> tuple[int, int]:
        """
        Converts a node hash value into its corresponding x and y coordinates in the grid.

        Parameters:
            node_hash_value (int): The hash value of the node.

        Returns:
            tuple[int, int]: The x and y coordinates of the node in the grid.
        """
        x = node_hash_value // self.grid_width
        y = node_hash_value % self.grid_width
        return x, y

    def build_adjacency_list(self):
        """
        Builds the adjacency list based on the coordinates list.

        The method iterates over each coordinate in the coordinates list and calculates
        the hash value for the node. It then adds the block type to the adjacency list
        using the hash value as the key.
        """
        for x, y, block_type in self.coordinates_list:
            node_hash_value = self.node_hash_function(x, y)
            self.adjacency_list[node_hash_value] = block_type

    def printMaze(self):
        """
        Print out an ascii representation of the maze.
        A * indicates a wall and a empty space indicates an open space in the maze
        """

        # Please complete this method to perform the above described function
        if not self.is_adjacency_list_built:
            self.build_adjacency_list()

        maze_str = ""

        for i in range(self.grid_height):
            for j in range(self.grid_width):
                node_hash_value = self.node_hash_function(i, j)
                if (
                    node_hash_value in self.adjacency_list.keys()
                    and self.adjacency_list[node_hash_value] == 0
                ):
                    maze_str += " "
                else:
                    maze_str += "*"
            maze_str += "\n"

        print(maze_str)

    def is_coordinates_within_grid(self, x: int, y: int):
        """
        Check if the given coordinates (x, y) are within the grid.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if the coordinates are within the grid, False otherwise.
        """
        return 0 <= x < self.grid_height and 0 <= y < self.grid_width

    def get_node_neighbors(self, node_hash_value: int):
        """
        Returns a list of hash values representing the neighbors of a given node.

        Parameters:
        - node_hash_value (int): The hash value of the node.

        Returns:
        - node_neighbors (list): A list of hash values representing the neighbors of the node.
        """
        x, y = self.node_inverse_hash_function(node_hash_value)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        node_neighbors = []
        for delta_x, delta_y in zip(dx, dy):
            new_x = x + delta_x
            new_y = y + delta_y
            if self.is_coordinates_within_grid(new_x, new_y):
                node_neighbors.append(self.node_hash_function(new_x, new_y))
        return node_neighbors

    def reconstruct_path(self, destination_node, parent_node_map):
        """
        Reconstructs the path from the destination node to the starting node using the parent node map.

        Args:
            destination_node (int): The destination node.
            parent_node_map (dict): A dictionary mapping each node to its parent node.

        Returns:
            list: The reconstructed path as a list of nodes.
        """
        path = []
        current_node = destination_node
        while current_node != -1:
            path.append(self.node_inverse_hash_function(current_node))
            current_node = parent_node_map[current_node]
        return path[::-1]

    def findRoute(self, x1, y1, x2, y2):
        """
        This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
        It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
        in the order in which the coordinates must be followed
        If no route is found, return an empty list
        """
        if not self.is_adjacency_list_built:
            self.build_adjacency_list()

        start_node = self.node_hash_function(x1, y1)
        destination_node = self.node_hash_function(x2, y2)

        stack = [start_node]
        visited_nodes = set()
        parent_node_map = {}

        visited_nodes.add(start_node)
        parent_node_map[start_node] = -1

        destination_reached = False

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node == destination_node:
                destination_reached = True
                break

            neighbor_nodes = self.get_node_neighbors(current_node)

            for neighbor_node in neighbor_nodes:
                if (
                    neighbor_node not in visited_nodes  # node not visited
                    and neighbor_node
                    in self.adjacency_list.keys()  # node in adjacency list
                    and self.adjacency_list[neighbor_node] == 0
                ):  # node is an open space not wall
                    visited_nodes.add(neighbor_node)
                    stack.append(neighbor_node)
                    parent_node_map[neighbor_node] = current_node

        if destination_reached:
            return self.reconstruct_path(destination_node, parent_node_map)
        else:
            return []


def morseCodeTest():
    """
    This test program passes the morse code as a list of strings for the word
    HELLO to the decode method. It should receive a string "HELLO" in return.
    This is provided as a simple test example, but by no means covers all possibilities, and you should
    fulfill the methods as described in their comments.
    """

    hello = ["....", ".", ".-..", ".-..", "---"]
    test = ["-", ".", "...", "-"]

    print(morseDecode(hello))
    print(morseDecode(test))


def partialMorseCodeTest():
    """
    This test program passes the partial morse code as a list of strings
    to the morsePartialDecode method. This is provided as a simple test example, but by
    no means covers all possibilities, and you should fulfill the methods as described in their comments.
    """

    # This is a partial representation of the word TEST, amongst other possible combinations
    test = ["x", "x", "x..", "x"]
    print(morsePartialDecode(test))

    # This is a partial representation of the word DANCE, amongst other possible combinations
    dance = ["x..", "x-", "x.", "x.-.", "x"]
    print(morsePartialDecode(dance))


def mazeTest():
    """
    This sets the open space coordinates for an example
    maze for the testing purpose in the assignment.
    The remainder of coordinates within the max bounds of these specified coordinates
    are assumed to be walls
    """
    myMaze = Maze()

    myMaze.addCoordinate(0, 0, 0)
    myMaze.addCoordinate(0, 1, 1)
    myMaze.addCoordinate(0, 2, 1)

    myMaze.addCoordinate(1, 0, 0)
    myMaze.addCoordinate(1, 1, 1)
    myMaze.addCoordinate(1, 2, 1)

    myMaze.addCoordinate(2, 0, 0)
    myMaze.addCoordinate(2, 1, 0)
    myMaze.addCoordinate(2, 2, 1)
    myMaze.addCoordinate(2, 3, 1)

    myMaze.addCoordinate(3, 0, 1)
    myMaze.addCoordinate(3, 1, 0)
    myMaze.addCoordinate(3, 2, 0)
    myMaze.addCoordinate(3, 3, 0)

    myMaze.addCoordinate(4, 0, 1)
    myMaze.addCoordinate(4, 1, 0)
    myMaze.addCoordinate(4, 2, 0)
    myMaze.addCoordinate(4, 3, 0)

    myMaze.printMaze()

    route = myMaze.findRoute(0, 0, 4, 3)

    print(route)


def main():
    # morseCodeTest()
    partialMorseCodeTest()
    # mazeTest()


if __name__ == "__main__":
    main()
