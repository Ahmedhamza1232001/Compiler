class SympolTable():
    Terminals={'chars':['a','b','epsilon'],'digits':['1','2','3'],'operator':['+','-','/','*']}
    NonTerminals=['A','B','S']
    TypeLength={'int':2,'char':4}

    def CreateSymbolTabel(self,text):
        symobolTabel={}
        lines=text.split('\n')
        lineNumber=1
        address=0
        count=1
        for line in lines:
            for char in line:
                if char ==" " or char=="'" or char=='=' or char in self.Terminals['digits']:
                    continue
                if char in symobolTabel.keys():
                    symobolTabel[char]["line Reference"].append(count)
                else:
                    symobolTabel[char]={"counter":count,"lineOfDeclaration":lineNumber,"variableName":char,"address":address,"numberOfDimensions":1,
                        "line Reference":[]}

                    # setting the data type value
                    if char in self.Terminals['chars']:
                        symobolTabel[char].update({"DataType":'char'})
                    elif char in self.Terminals['digits']:
                        symobolTabel[char].update({"DataType":'int'})
                    elif char in self.NonTerminals:
                        symobolTabel[char].update({"DataType":'char'})
                    # udating the address
                    if symobolTabel[char]["DataType"]=='int':
                        address=address+2
                    if symobolTabel[char]["DataType"]=='char':
                        address+=4

            lineNumber+=1
            count+=1
        return symobolTabel
    
input="a = 3 \nb=b\nA=a  "    
symbolT=SympolTable()
s=symbolT.CreateSymbolTabel(input)
print(s)

