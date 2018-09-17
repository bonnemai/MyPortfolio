
import math
debug=False

def solution(N):
    _bin=bin(N)
    if debug: print(_bin)
    _zeros=''
    max_nb_zero=int(math.log(N+1)/math.log(2))
    for i in range(0, max_nb_zero):
        _zeros+='0'
    for i in range(1, max_nb_zero):
        # _str=get_str(N-i)
        _zeros=_zeros.replace('0', '', 1)
        _str='1'+_zeros+'1'
        if _str in _bin:
            return max_nb_zero-i
    return 0



print('1041: '+str(solution(1041)==5))
print('328: '+str(solution(328)==2))
print('15: '+str(solution(15)==0))
print('32: '+str(solution(32)==0))
print('2**31-1: '+str(solution(2**31-1)==0))