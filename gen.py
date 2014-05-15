from itertools import combinations_with_replacement, permutations
from sys import argv

# str -> int
def num(i):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    val = alphabet.find(i)
    if val == -1 :
        exit_('Not supported : %s, allowed : [0123456789abcdefghijklmnopqrstuvwxyz]'%i)
    return(val)

# array of ints -> str
def str__(n):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    return( alphabet[n] )

def valid(seq, t):
    permutation_seq = [ ((h+p)%t) for p,h in enumerate(seq) ]
    return(len(set(permutation_seq)) == t)

output = open('out','w')

N = int(argv[1])
H = num(argv[2])
P = int(argv[3])


heights = [ str__(h) for h in range(H+1)]

valids = set([str(N)])
current = 0
for i in range(P) :
    ii = i+1
    gen = combinations_with_replacement( heights , ii )
    for comb in gen :
        # (ii == len(comb))
        comb = [ num(n) for n in comb]
        if 1.*sum( comb )/ii == N :     
            for p in set(permutations(comb)) :
                seq = ''.join([str__(n) for n in p ])
                if valid(p, ii) :
                    valids.add(seq)
                    output.write(seq+'\n')
                    current += 1
                    if current % 5000 == 0 :
                        print 'Permutations generated : '+str(current)
print 'Permutations generated : '+str(current)


# gen = combinations_with_replacement( heights , P )
# for comb in gen :
#     # (ii == len(comb))
#     comb = [ num(n) for n in comb]
#     if 1.*sum( comb )/P == N :     
#         for p in set(permutations(comb)) :
#             seq = ''.join([str__(n) for n in p ])
#             if valid(p, P) :
#                 valids.add(seq)
#                 output.write(seq+'\n')
#                 current += 1
#                 if current % 5000 == 0 :
#                     print 'Permutations generated : '+str(current)
# print 'Permutations generated : '+str(current)