input_string = "int x eql 5 ; int y eql 6 ; int z eql x add y ; flt z ; flt x"

splited_input = input_string.split(" ")
print(splited_input)
length = len(splited_input)

resreved_words={
                "int":1,  "1":11,
                "flt":2,  "2":12,
                "bol":3,  "3":13,
                "add":4,  "4":14,
                "mlt":5,  "5":15,
                "eql":6,  "6":16,
                "prt":7,  "7":17,
                "x"  :8,  "8":18,
                "y"  :9,  "9":19,
                "z"  :10, "0":20,
                "("  :21, ")":22,
                ";":23,
                             
                }

##lexical analysis 
# old_i=0
# for i in range (length):
#     newline=[]    
#     if(splited_input[i] == ";"):        
#         newline.extend(splited_input[old_i+1:i]) 
#         old_i=i
#     else :
#         continue
#     print(newline)
#     for word in range(len(newline)):
#         print(resreved_words[newline[word]])    


### parse tree 
# input_grammar = "( x add y ) mlt z"
# splited_grammar = input_grammar.split(" ")
# gl=len(splited_grammar)
# old_j=0
# print ("staatment\n|")

# for m in range (gl):
#     prances=[]  
#     if(splited_grammar[m] == "(" or splited_grammar[m] == ")" ):        
#         prances.append(splited_grammar[old_j+1:m]) 
#         old_j=m
#         print(" node is " + "expression "+ splited_grammar[m])
#     elif(splited_grammar[m] == "mlt" or splited_grammar[m] == "add" ):
#         print("   node is " + "operation "+"\n   |  \n   "+  splited_grammar[m])  
#     elif(splited_grammar[m] == "x" or splited_grammar[m] == "y" or splited_grammar[m] == "z" ):
#         print("   node is " + "var "+ "\n  |  \n   "+ splited_grammar[m])        
#     else :
#         continue
    
 
#sympol table

# old_i = 0
# line_counter = 0
# address=0
# for i in range (length):
#     newline=[]    
#     if(splited_input[i] == ";"):        
#         newline.extend(splited_input[old_i+1:i]) 
#         old_i=i
#         line_counter+=1
#     elif (splited_input[i] == "int"):
#         type="intger"
#         address+=2
#         print(address,line_counter,"name",splited_input[i+1],type)
#     elif (splited_input[i] == "bol"):
#         type="boolean"
#         address+=1
#         print(address,line_counter,"name",splited_input[i+1],type)
#     elif (splited_input[i] == "flt"):
#         type="float"
#         address+=4
#         print(address,line_counter,"name",splited_input[i+1],type)
