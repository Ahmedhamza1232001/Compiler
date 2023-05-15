class parseTree:
    Terminals={'chars':['a','b','c','d'],'operator':['+','-','='],'digits':['1','2']}
    NonTreminals=['S','A', 'B']

    def AssignmentParser(self,lexemes):
        lexemes=lexemes.split()
        tree={'root':"assignment"}
        
        left=lexemes.pop(0)
        if left not in self.Terminals['chars'] and  left not in self.NonTreminals:
            raise ValueError("the variable name: "+ left +" is not a valid name in this language")
        else:    
            tree.update({'left':left})
        
        operator=lexemes.pop(0)
        if operator != '=':
            raise ValueError("the operator: "+ operator +" equlity operator use{ = }instead")
        else:
            tree.update({'operator':'='})
        
        ExpressionValue=self.Check_ex(lexemes)
        tree.update({'right':ExpressionValue})

        return tree

    def Check_ex(self,lexemes):
        if len(lexemes)==1:
            return lexemes.pop()
        else:
            tree={}

            left=lexemes.pop(0)
            if left not in self.Terminals['digits']:
                raise ValueError("the value "+left +" isn't integer so it cant be added")
            else:
                tree.update({'left':left})

            operator=lexemes.pop(0)
            if operator == '=':
                raise ValueError("you cant use assignment in the right hand side")
            else:
                tree.update({'operator':operator})
            
            right=lexemes.pop(0)
            if left not in self.Terminals['digits']:
                raise ValueError("the value "+right +" isn't integer so it cant be added")
            else:
                tree.update({'right':right})

            return tree
# S = 1 + 2
input=' S = 1 + 2'
syntaxAnalyzer=parseTree()
x=syntaxAnalyzer.AssignmentParser(input)
print(x)