import math

def delete(S, T):
    for letter in S:
        new_word=S.replace(letter, '', 1)
        if new_word==T:
            return letter
    return None


def swap(S, T):
    ''' TODO: Check i>1... '''
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            new_word=list(S)
            letter1=new_word[i]
            letter2=new_word[j]
            new_word[i]=letter2
            new_word[j]=letter1
            if ''.join(new_word)==T:
                return 'SWAP ' +letter1 + ' ' + letter2
    return 'IMPOSSIBLE'

print(swap('ab', 'ba'))
print(swap('abc', 'bac'))
print(swap('cab', 'cba'))
print(swap('cccccab', 'cccccba'))
print(swap('cab', 'dba')=='IMPOSSIBLE')

def solution(S, T):
    if S==T:
        return "NOTHING"
    elif math.fabs(len(S)-len(T))>1:
        return "IMPOSSIBLE"
    elif len(S)>len(T):
        # Try to DELETE¸
        _del=delete(S, T)
        if _del is None:
            return "IMPOSSIBLE"
        else:
            return "DELETE "+_del
    elif len(S)<len(T):
        # Try to INSERT: equivalent of delete...
        _del=delete( T, S)
        if _del is None:
            return "IMPOSSIBLE"
        else:
            return "INSERT "+_del
    elif len(S)==len(T):
        # Try to Swap
        return swap(S, T)
    return None

print(delete('niece', 'nice')=='e')
print(solution('niece', 'nice')=='DELETE e')
print(delete('abcd', 'efg')is None)
print(solution('abcd', 'efg')=='IMPOSSIBLE')
print(solution('nice', 'niece')=='INSERT e')
print(solution('form', 'from')=='SWAP o r')
print(solution('o', 'odd')=='IMPOSSIBLE')
print(solution('odd', 'odd')=='NOTHING')
print(solution('odd', 'odd1')=='INSERT 1')
print(solution('odd1', 'odd')=='DELETE 1')
print(solution('o', 'abcderfede')=='IMPOSSIBLE')