import re

# Define the context-free grammar
grammar = {
    "S": [["N", "V", "O"]],
    "N": [["John"], ["Mary"]],
    "V": [["likes"], ["hates"]],
    "O": [["pizza"], ["spaghetti"]]
}

# Define a regular expression for matching terminals
terminal_regex = r'"[^"]+"|\w+'

# Define a function to parse a string according to the grammar
def parse_string(string):
    # Split the string into words
    words = re.findall(terminal_regex, string)

    # Initialize a stack with the start symbol
    stack = ["S"]

    # Initialize an empty list to store the parse tree nodes
    nodes = []

    # Iterate over the words and the stack
    while stack:
        # Get the next word and symbol from the top of the stack
        word = words.pop(0)
        symbol = stack.pop()

        # Check if the symbol is a non-terminal
        if symbol in grammar:
            # Get the list of productions for the non-terminal
            productions = grammar[symbol]

            # Iterate over the productions and push the RHS symbols onto the stack in reverse order
            for production in reversed(productions):
                # Push the RHS symbols onto the stack
                for rhs_symbol in production:
                    stack.append(rhs_symbol)

                # Append the LHS symbol and the RHS symbols to the nodes list
                nodes.append((symbol, production))
        else:
            # If the symbol is a terminal, check if it matches the current word
            if symbol == word:
                # If the word matches, append the word and symbol to the nodes list
                nodes.append((symbol, word))
            else:
                # If the word does not match, raise a syntax error
                raise SyntaxError(f"Expected '{symbol}', but found '{word}'")

    # Return the list of parse tree nodes
    return nodes

# Define an example string to parse
string = "John likes pizza"

# Parse the string and print the list of nodes
nodes = parse_string(string)
print(nodes)
