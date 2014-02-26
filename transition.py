from sys import argv
from itertools import permutations

VERBOSE = False

if len(argv) != 2 :
    exit('usage ex : transition.py 771') 

# str -> array of ints
def num(i):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    val = alphabet.find(i)
    if val == -1 :
        exit('Not supported : %s, allowed : [0123456789abcdefghijklmnopqrstuvwxyz]'%i)
    return(val)

# array of ints -> str
def str_(a):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    return(''.join([ alphabet[i] for i in a ]))

# check for the sequence's validity
def valid(seq):
    t = len(seq)
    permutation_seq = [ ((h+p)%t) for p,h in enumerate(seq) ]
    return(len(set(permutation_seq)) == t)


# Extract an array of heights from the string
sequence = [ num(i) for i in argv[1] ]
sequences = [sequence]

# exit if the siteswap isn't valid
if not valid(sequence) :
    sequences = []
    print('Invalid siteswap sequence, you could try one of theses :')
    for p in permutations(sequence) :
        if valid(p) :
            #print(''.join([ str_(h) for h in p]))    
            sequences.append(p)

    #exit()

# add one event in position i in the time-line a
def set_taken(i,a):
    if i < len(a):
        a[i] = True
    else :
        for i in range(i-len(a)):
            a.append(False)
        a.append(True)

# determine the state of the sequence
def seq_state(sequence):
    n = sum(sequence)/len(sequence)
    state = []
    while len([ p for p in state if p ]) < n :
        for h in sequence :
            set_taken(h,state)
            state = state[1:]
            if VERBOSE : print(state)   
    return(state)

# determine the transition to enter the state of the sequence from the base state
def base_state_to_seq_state(state):
    n = len([ h for h in state if h])
    e = 0
    entrance = []
    for i in state :
        if i :
            entrance.append(n+e)
        else :
            e += 1
    while entrance[0] == n :
        entrance = entrance[1:]
    return(entrance)

# determine the transition to enter the base state from the state of the sequence
def seq_state_to_base_state(state):
    exit = []
    while len([ p for p in state if not p ]) > 0 :
        h = state.index(False)
        exit.append(h)
        set_taken(h,state)
        state = state[1:]
    return(exit)

# Now, let's get to work
for sequence in sequences :

    state = seq_state(sequence)
    entrance = base_state_to_seq_state(state)
    exit = seq_state_to_base_state(state)

    print(str_(entrance)+'('+str_(sequence)+')'+str_(exit))
