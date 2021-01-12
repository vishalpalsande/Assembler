 # Assembler(One Pass Assembler) 
 
 >## This assembler generates files : 
 #### 1.Symbol Table
 #### 2.Literal Table
 #### 3.Intermediate Code

#

>## Project Statistic:

**Platform** : Linux

**Technology** : Python, Assembly language

**Type** : CUI

#

> assembler.py is a main driver code. 
  
  To run this code type command,

        python3 assembler.py {action} {filename}


where, assembler.py is a driver code actions are **( -s ,-l ,-i )** 

**-s** -> For symbol table   
**-l** -> For literal table    
**-i** -> For intermediate table 

When -i option is selected, 
additional **'IntermediateTable.txt'** file will be generated. 
This file contains the intermediate code.

#
