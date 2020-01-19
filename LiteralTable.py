def LiteralTable(list1):
    literal = []
    count_literal = 1
    for i in range(len(list1)):
        if len(list1[i]) > 2:
            if list1[i][1] in ['dw','dd','dq','dt']:
                literal.append([i+1, 'lit#'+str(count_literal), list1[i][2], hex1(list1[i][2])])
                count_literal += 1
            elif list1[i][1] == 'db':
                literal.append([i+1, 'lit#'+str(count_literal), list1[i][2], hex2(list1[i][2])])
                count_literal += 1
            if (list1[i][1] not in ['resb','resw','resd','resq','rest','db','dw','dd','dq','dt']) and ((list1[i][2]).isdigit() == True):
                literal.append([i+1, 'lit#'+str(count_literal), list1[i][2], hex1(list1[i][2])])
                count_literal += 1
    return(literal)

def hex1(arg1):
    temp = arg1.split(",")
    temp2 = [] 
    for i in temp:
        if int(i) in [0,1,2,3,4,5,6,7,8,9]:
            tempp = ('0'+i)
            tempp = (tempp) + '0'*(8- len(tempp))
            temp2.append(tempp)
        elif int(i) == 10:
            tempp = ('0'+str(hex(int(i)))[2:])
            tempp = (tempp) + '0'*(8- len(tempp))
            temp2.append(tempp)
        else:
            a = str(hex(int(i)))
            tempp = a[2:]
            tempp = (tempp) + '0'*(8- len(tempp))
            temp2.append(tempp)

    temp2 = "".join(temp2)
    return temp2

def hex2(arg1):
    temp = arg1.split(',')
    temp2 = ''
    for i in temp:
        print(i)
        if i.isdigit() == True:
            a = hex1(i)
            temp2 += a
        else:
            for j in temp[i]:
                print(j)
    return temp3

def hex2(arg1):
    temp = arg1.split(',')
    temp2 = ''
    for i in range(len(temp)):
        if temp[i].isdigit() == True:
            a = hex1(temp[i])
            temp2 += a
        else:
            for j in range(len(temp[i])):
                if (j == 0) or (j == (len(temp[i])-1)):
                    pass
                else:
                    a = hex(ord(temp[i][j]))
                    a = a[2:]
                    temp2 += str(a)
    return temp2
