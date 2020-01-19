from sys import argv
from validation import *
from SymbolTable import *
from LiteralTable import *
from IntermediateTable import *

script,action,filename = argv
#-----------------------------------
validation(action)
#-----------------------------------

with open(filename,'r') as f:
    list1 = []
    for line in f:
        line = line.strip()
        line = line.split(' ')
        list1.append(line)
for i in range(len(list1)):
    if (len(list1[i])>2):
        if list1[i][1] == 'db':
            list1[i][2] = " ".join(list1[i][2:])
            list1[i] = list1[i][:3]
        if list1[i][1] in data_type:
            list1[i][2] = "".join(list1[i][2:])
            list1[i] = list1[i][:3]
#-------------------------------------------------------------------------------------------------------------------------------
#symbol table
(symbol_table,label_table) = SymbolTable(list1)
if (action == '-s'):
    print('\n')
    print("                                                      ###### SYMBOL TABLE ######                                                  ")
    print("==================================================================================================================")
    print('LineNo.     SymbolName          Size       No.OfElements         Def/Undef              Value')
    print("==================================================================================================================")
    for i in symbol_table:
        for j in i:
            print(j,end='\t\t')
        print('\n')
    print('\n')
    print("              ###### LABEL TABLE #######                ")
    print("========================================================")
    print("LineNo.         LabelNo        LableName      Def/Undef")
    print("========================================================")
    for i in label_table:
        for j in i:
            print(j, end='\t\t')
        print('\n')
#----------------------------------------------------------------------------------------------------------------------------------
#literal table
lit_table = LiteralTable(list1)
if (action == '-l'): 
    print('\n')
    print("                                                ###### LITERAL TABLE ######                                            ")
    print("=============================================================================================================================")
    print("LineNo.               LiteralNo.                 Actual_value                 Hex Value")
    print("=============================================================================================================================")
    for i in lit_table:
        for j in i:
            print(j, end='\t\t\t')
        print('\n')
#----------------------------------------------------------------------------------------------------------------------------------
if (action == '-i'):
    IntermediateTable(list1,symbol_table,label_table,lit_table)
    print("Intermediate text file is created")
#----------------------------------------------------------------------------------------------------------------------------------
