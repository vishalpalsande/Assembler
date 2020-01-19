data_type = ['dw','dd','dq','dt']
bss_type = ['resb','resw','resd','resq','rest']
size_dict = {'db':1, 'dw':2, 'dd':4, 'dq':8, 'dt':10, 'resb':1, 'resw':2, 'resd':4, 'resq':8, 'rest':10}
#size_dict2 = {'eax':000, 'ecx':001, 'edx':010, 'ebx':011, 'esp':100, 'ebp':101, 'esi':110, 'edi':111}
jump = ['jmp','jne','je','jgt','jge','jlt','jle']
def SymbolTable(list1):
    symbol = []
    label = []
    data_addr = 0
    bss_addr = 0
    for i in range(len(list1)):
        if (len(list1[i])>2):
            if (list1[i][1] in data_type + ['db']):
                number = length(list1[i][1],list1[i][2])
                size = number * size_dict[list1[i][1]] 
                symbol.append([i+1, list1[i][0], size_dict[list1[i][1]], number+1,'Def',list1[i][2]])
                data_addr = data_addr + size
            if (list1[i][1] in bss_type):
                number = int(list1[i][2])
                size = number * size_dict[list1[i][1]] 
                symbol.append([i+1, list1[i][0], size_dict[list1[i][1]], number,'Undef','-'])
                bss_addr = bss_addr + size

    defined_labels = []
    temp_label = []
    for i in range(len(list1)):
        if (list1[i][0] != '') and ((list1[i][0][len(list1[i][0])-1]) == ':'):
            defined_labels.append(list1[i][0][:len(list1[i][0])-1])
    count_label = 1
    for i in range(len(list1)):
        if (len(list1[i]) > 1):
            if (list1[i][0] == 'global') or (list1[i][0] in jump):
                if (list1[i][1] in defined_labels) and (list1[i][1] not in temp_label):
                    label.append([i+1, 'label#'+str(count_label), list1[i][1], 'Def'])
                    count_label += 1
                    temp_label.append(list1[i][1])
                else:
                    label.append([i+1, 'label#'+str(count_label), list1[i][1], 'Undef'])
                    count_label += 1
        if ((list1[i][0][:len(list1[i][0])-1]) in defined_labels) and ((list1[i][0][:len(list1[i][0])-1]) not in temp_label):
            label.append([i+1, 'label#'+str(count_label), list1[i][0][:len(list1[i][0])-1], 'Def'])
            count_label += 1
            temp_label.append(list1[i][0][:len(list1[i][0])-1])

    return (symbol, label)

def length(arg1,arg2):
    if arg1 in data_type:
        temp1 = arg2.split(',')
        return len(temp1)
    if arg1 == 'db':
        temp1 = arg2.split(',')
        len1 = len(temp1) - 1
        len1 = (len(temp1[0])-2) + len1
        return len1

