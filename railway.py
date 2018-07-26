
def get_subset(s1):
    results=[]
    for i in range(1, len(s1)+1):
        for j in range(len(s1)-i+1):
            s2=int(s1[j:j+i])
            results.append(s2)
    return results

def is_prime(nb):
    if nb in [0, 1]:
        return True
    for i in range(2, nb-1):
        if nb%i==0:
            return False
    return True

def railway(arr):
    ''' Max nb occurence of a prime number in the subset of a list of numbers'''
    prime_result={}
    prime_nb={}
    for a in arr:
        subset=get_subset(str(a))
        for s in subset:
            if s in prime_result:
                s_prime=prime_result[s]
            else:
                s_prime=is_prime(s)
                prime_result[s]=s_prime
            if s_prime:
                if s in prime_nb:
                    prime_nb[s]+=1
                else:
                    prime_nb[s]=1

    max_nb_occurence_prime=0
    for key in prime_nb:
        if prime_nb[key]>max_nb_occurence_prime:
            max_nb_occurence_prime=prime_nb[key]
    return max_nb_occurence_prime

print(railway([123, 321, 23, 25, 23]))