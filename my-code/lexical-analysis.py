import re
# Define the input code
input_code = "int _x=5;"

# Define a list of keywords
keywords = ["int"]

# Define a list of separators
separators = ["=", ";"]

# Define a regular expression for matching integer literals
integer_regex = r"\d+"

# Define a regular expression for matching identifier names
identifier_regex = r"[a-zA-Z_][a-zA-Z0-9_]*"

# Define a function to tokenize the input code
def tokenize(code):
    # Initialize an empty list to store the tokens
    tokens = []

    # Split the input code into words
    words = code.split()

    # Iterate over the words and identify the tokens
    for word in words:
        # Check if the word is a keyword
        if word in keywords:
            tokens.append(("keyword", word))
        # Check if the word is a separator
        elif word in separators:
            tokens.append(("separator", word))
        # Check if the word is an integer literal
        elif re.match(integer_regex, word):
            tokens.append(("integer", int(word)))
        # Check if the word is an identifier
        elif re.match(identifier_regex, word):
            tokens.append(("identifier", word))
        # Otherwise, raise an error for an invalid token
        else:
            raise ValueError(f"Invalid token: {word}")

    # Return the list of tokens
    return tokens

# Call the tokenize function with the input code
tokens = tokenize(input_code)

# Print the list of tokens
print(tokens)