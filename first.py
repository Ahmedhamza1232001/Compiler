"""
S=>Ac
A=>B
B=>b|e
C=>c|e
"""
class First():
    terminals=['a', 'b','c']
    nonterminals=['A','B','C','Q']
    # the [] implies 'epsilon'
    production_rules={'A':['B'],'B':['b',[]],'C':['c',[]],'S':['AC'],'Q':[]}

    def calculate_first(self, non_terminal):
        first_set = set()

        # If the non-terminal is a terminal symbol, add it to the first set
        if non_terminal in self.terminals:
            first_set.add(non_terminal)
            return first_set

        # Otherwise, iterate over all production rules for the non-terminal
        for production_rule in self.production_rules[non_terminal]:
            # If the production rule is epsilon, add it to the first set
            if production_rule == []:
                first_set.add('epsilon')
                continue

            # Otherwise, iterate over all symbols in the production rule
            for symbol in production_rule:
                # If the symbol is a terminal symbol, add it to the first set and break
                if symbol in self.terminals:
                    first_set.add(symbol)
                    break
                # Otherwise, recursively calculate the first set for the non-terminal and add it to the first set
                else:
                    symbol_first_set =self.calculate_first(symbol)

                    if 'epsilon' in symbol_first_set and symbol!=production_rule[-1]:
                        symbol_first_set.remove('epsilon')

                    first_set |= symbol_first_set

        return first_set

first= First()
first=first.calculate_first('S')
print(first)
