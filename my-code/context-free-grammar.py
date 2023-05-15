# Define a function to parse a sentence and create a parse tree
def parse_sentence(grammar, sentence):
    # Tokenize the sentence by splitting on whitespace
    tokens = sentence.split()

    # Define a recursive function to parse a sentence and create a parse tree
    def draw_tree(parse_tree, indent='='):
        print("Drawing tree for:", parse_tree)
        if isinstance(parse_tree, str):
            print(indent + parse_tree)
        else:
            print(indent + parse_tree[0])
            for subtree in parse_tree[1:]:
                draw_tree(subtree, indent + '  ')

    # Call the parse_tree function with the start symbol and sentence tokens
    parse_tree = parse_tree('S', tokens)

    # Define a function to draw the parse tree recursively
    def draw_tree(parse_tree, indent=''):
        if parse_tree is None:
            print("Error: could not parse sentence")
        elif isinstance(parse_tree, str):
            print(indent + parse_tree)
        else:
            print(indent + parse_tree[0])
            for subtree in parse_tree[1:]:
                draw_tree(subtree, indent + '  ')

    # Call the draw_tree function with the parse tree
    draw_tree(parse_tree)
