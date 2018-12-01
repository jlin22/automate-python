import re

def my_strip(s, chars=' '):
    ''' my version of the string strip function '''

    # copy s
    a = ''
    for c in s:
        a += c

    reg_str = r'(' 
    for i in range(len(chars)):
        reg_str += chars[i]
        if i != len(chars) - 1:
            reg_str += '|'
    reg_str += ")+"

    begin_re = re.compile(r'^' + reg_str)
    end_re = re.compile(reg_str + r'$')
    print(reg_str)

    while True:
        old = a
        a = re.sub(begin_re, '', a)
        if old == a: break

    while True:
        old = a
        a = re.sub(end_re, '', a)
        if old == a: break

    return a

print(my_strip(' xxxxxyyyyyyThere is no passwordyyyyyzzzxxxxx   ', chars='xyz '))
