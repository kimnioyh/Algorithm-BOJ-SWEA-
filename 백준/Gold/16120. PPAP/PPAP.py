chars = input()
ppapstack = []
res = 'NP'

for char in chars :
    if char == 'P':
        if ppapstack and ppapstack[-1] == 'A':
            ppapstack.pop()
            ppapstack.pop()
        else :
            ppapstack += ['P']
    if char == 'A':
        if len(ppapstack) < 2:
            break
        else :
            ppapstack += ['A']
else :
    if ppapstack == ['P']:
        res = 'PPAP'
print(res)