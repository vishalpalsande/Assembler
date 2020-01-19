 This is one pass Assembler written in python.
 
 this assembler generates files : 
 1.Symbol Table
 
 2.Literal Table
 
 3.Intermediate Code

> assembler.py is a main driver code. 
  
  To run code type,

        python3 assembler.py {action} {filename}


where, assembler.py is a driver code actions are (-s,-l,-i) 

-s -> For symbol table   
-l -> For literal table    
-i -> For intermediate table 

When -i option is selected, 
additional 'IntermediateTable.txt' file will be generated. 
This file contains the intermediate code.

