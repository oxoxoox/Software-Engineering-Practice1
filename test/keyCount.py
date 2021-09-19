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
    num = 0
    kw_list = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
               'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
               'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
               'static', 'struct', 'switch', 'typedef', 'union', 'unsigned',
               'void', 'volatile', 'while']
    for key in kw_list:
        n = code.count(key)
        num += n
    print("total num: " ,num)

if __name__ == '__main__':
    path='../data/code1.c'
    code = read_file(path)
    cout_keys(code)