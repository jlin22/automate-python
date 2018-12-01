import re

def permutations(a):
    ''' assume a has len == 3 '''
    x, y, z = a[0], a[1], a[2]
    return [[x, y, z], [x, z, y], [y, x, z], [y, z, x], [z, x, y], [z, y, x]]


def strong_pass(password):
    ''' Determines if a password is strong, i.e.
    upper case and lower case, and 1 digit '''
    # come up with the 3! permutations of upper, lower, digit
    reqs = [r'[A-Z]+', r'[a-z]+', r'\d+']
    perms = permutations(reqs)
    for i in range(len(perms)):
        perms[i] = (r'.*').join(perms[i])
    strong = False
    for p in perms:
        regexp = re.compile(p)
        mo = regexp.match(password)
        if mo:
            strong = True
            break
    return strong
        
a = [1, 3, 5]
print(permutations(a))
print(strong_pass('xyz'))
print(strong_pass('helloKitty123'))
print(strong_pass('rith12Alg'))
    

