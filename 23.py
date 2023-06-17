def f(x, mulcount=0, prog = ''):
    if x == 11:
        print(prog)
        return 1
    if x > 11:
        return 0
    count = f(x + 1, 0, prog + ' +1') + f(x + 2, 0, prog + '+2')
    if mulcount == 0:
        count +=1