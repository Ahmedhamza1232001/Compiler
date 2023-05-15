import re

pattern1 = r'\=|\+|\-|\*|\;|\w+|\".+?\"'
pattern = r'\=|\+|\-|\*|\;|\w+|\".+?\"'

code = ''''
str x;
int v = 5;
print "hello";
x = 3;
'''

token = {
    "int": "type",
    "str": "type",
    "print": "keyword",

    "=": "operator",
    "+": "operator",

    ";": "delimiter"
}

match = re.findall(pattern, code)

file = open('f.txt', 'w')
print(match)
code_list = []
for mat in match:
    file.write(mat + '\n')
    code_list.append(mat)

print(f"lexeme: {code_list}")

tokens = []
for items in code_list:
    if items in token:
        tokens.append(token[items])
    elif items.startswith('"') and items.endswith('"'):
        tokens.append("string")
    elif items.isdigit():
        tokens.append("num")
    else:
        tokens.append("id")

print(f"tokens: {tokens}")

line = 1
oca = 0

sym = []
var = []

for i in range(len(code_list)):
    if code_list[i] == ";":
        line += 1

    if code_list[i] == "str" or code_list[i] == "int":
        sym.append(
            {"name": code_list[i+1], "line": line, "type": code_list[i], "num.of D": 0, "OCA": oca, "ref": []}
        )
        var.append(code_list[i+1])

        if code_list[i] == "int":
            oca += 2
        else:
            oca += 4

    if code_list[i] in var:
        for variable in sym:
            if variable["name"] == code_list[i]:
                variable["ref"].append(line)
            if variable["line"] in variable["ref"]:
                variable["ref"].remove(variable["line"])

for i in sym:
    print(i)

