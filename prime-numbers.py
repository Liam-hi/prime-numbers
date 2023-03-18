p = [2]

def Primes(prime):
    l = [x * prime for x in p if x < prime]
    pl = p[:len(l)]
    test = sum(x for x in range(len(pl)) if l[x] % 2 == 0 or prime * 2 % pl[x] == 0)
    return test

# Print all prime numbers from 1 to 1000. 

for x in range(1, 1000, 2):
    if x != 1 and Primes(x) == 0:
        p.append(x)
        
print(p)
