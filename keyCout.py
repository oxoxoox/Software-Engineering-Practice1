import re
from sys import argv

# read source file and return code
def read_file(path):
    code = ''
    with open (path,'r',encoding='UTF-8') as file:
        codeList = file.readlines()
    for l in codeList:
        code += l.strip()+' '
    # remove code's string and annotation
    code = re.sub("\"([^\"]*)\"|\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/|\/\/.*", "", code)
    return code

# level 1 to count keys
def cout_keys(code):
    count = {}
    count_sum = 0
    key_list = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
               'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
               'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
               'static', 'struct', 'switch', 'typedef', 'union', 'unsigned',
               'void', 'volatile', 'while']
    for key in key_list:
        n = len(re.findall("[^0-9a-zA-Z\_]" + key + "[^0-9a-zA-Z\_]", code))
        if n != 0:
            count[key] = n
            count_sum += n
    print("total num: " ,count_sum)

# level 2 to count switch and case
def cout_switch(code):
    switch_num = 0
    case_num = []
    switch_list = re.finditer(r"\sswitch\([^)]*\)\s*{",code)
    for i in switch_list:
        switch_num += 1
        index = i.end()
        case_list = re.findall(r"\scase\s",code[index:])
        case_num.append(len(case_list))
    for j in range(switch_num-1):
        case_num[j] = case_num[j]-case_num[j+1]
    print("switch num: ",switch_num)
    print("case num:"," ".join([str(i) for i in case_num]))

# level 4 to count if-else and if-elseif-else
def cout_if_else(code,level):
    if_stack = []
    # if-else num
    if_else_num1 = 0
    # if-elseif-else num
    if_else_num2 = 0
    match_else_if = False
    #find all if、elseif、else
    all_list = re.findall(r"else if|\s*else[{\s][^i]|if", code)
    for i in range(len(all_list)):
        if all_list[i] == "if":
            if_stack.append(1)
        elif all_list[i] == "else if":
            if_stack.append(2)
        else:
            while True:
                if if_stack.pop() == 2:
                    match_else_if = True
                else:
                    break
            if match_else_if:
                if_else_num2 += 1
                match_else_if = False
            else:
                if_else_num1 += 1
    print("if-else num: ",if_else_num1)
    if level == 4:
        print("if-elseif-else num: ",if_else_num2)

if __name__ == '__main__':
    # read args
    path, level = argv[1], int(argv[2])
    code = read_file(path)
    if level == 1:
        cout_keys(code)
    elif level == 2:
        cout_keys(code)
        cout_switch(code)
    else:
        cout_keys(code)
        cout_switch(code)
        cout_if_else(code, level)