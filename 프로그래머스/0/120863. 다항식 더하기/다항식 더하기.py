def solution(polynomial):
    xterm = 0
    cterm = 0
    terms = polynomial.split(' ')
    for t in terms:
        if 'x' in t:
            if t == 'x':
                xterm += 1
            else:
                xterm += int(t[:-1])
        elif t == '+':
            pass
        else: cterm += int(t)
    if xterm != 0 and cterm != 0:
        if xterm != 1:
            return ''.join([str(xterm), 'x', ' + ', str(cterm)])
        else: return ''.join(['x', ' + ', str(cterm)])
    elif xterm ==0 and cterm != 0:
        return str(cterm)
    elif xterm != 0 and cterm ==0:
        if xterm != 1:
            return ''.join([str(xterm), 'x'])
        else: return  'x'
    else: return 0