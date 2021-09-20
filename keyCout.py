import re


def read_file(path):
    code = ''
    with open (path,'r',encoding='UTF-8') as file:
        codeList = file.readlines()
    for l in codeList:
        code += l.strip()+' '
    code = re.sub("\"([^\"]*)\"|\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/|\/\/.*", "", code)
    return code

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

# def search_if(code):
#     i = re.search(r"[^e]\s+if", code)
#     return i
#
# def search_else_if(code):
#     j = re.search("else if", code)
#     return j
#
# def search_esle(code):
#     k = re.search(r"\s*else[{\s][^i]", code)
#     return k

def cout_if_else(code):
    if_stack = []
    if_else_num1 = 0
    if_else_num2 = 0
    match_else_if = False
    #reg = r"[^e]\s+if|else if|\s*else[{\s][^i]"
    # while True:
    #     i = search_if(code)
    #     if i:
    #         if_stack.append(1)
    #         index_if = i.end()
    #         j = search_else_if(code[index_if:])
    #         while j:
    #             if_stack.append(2)
    #             j = search_else_if(code[j.end():])
    #         k = search_else(c)
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
    print("if-elseif-else num: ",if_else_num2)

if __name__ == '__main__':
    path = "data/code1.c"
    # level = input()
    code = read_file(path)
    cout_keys(code)
    cout_switch(code)
    cout_if_else(code)