class lexical():
    
    Terminals=['a','b','epsilon']
    NonTerminals=['A','B','S']
    ProductionRules={'S':['AaAb','BbBb'],'A':['epsilon'],'B':['epsilon']}

    def LexicalAnalyser(self,text):
        tokens=[]
        for char in text:
            if char in self.Terminals:
                tokens.append(char)
                continue
            if char  in self.NonTerminals:
                tokens.append(char)
                continue
            else:
                raise ValueError('the char : '+char+' is not a valid character') 
        return tokens

input='aaabbS'
lexer=lexical()
tokens = lexer.LexicalAnalyser(input)
print("the code is valid lexer")
print("the set of tokens are",tokens)
