from sys import argv
from itertools import permutations

VERBOSE = False
#VERBOSE = True

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

# determine the transition to enter the state of the sequence from the ground state
def ground_state_to_seq_state(state):
    n = len([ h for h in state if h])
    e = 0
    entry = []
    for i in state :
        if i :
            entry.append(n+e)
        else :
            e += 1
    while entry[0] == n :
        if len(entry) == 1 :
            break
        entry = entry[1:]
    return(entry)

# determine the transition to enter the ground state from the state of the sequence
def seq_state_to_ground_state(s):
    state = [ h for h in s]
    exit = []
    while len([ p for p in state if not p ]) > 0 :
        h = state.index(False)
        exit.append(h)
        set_taken(h,state)
        state = state[1:]
    return(exit)


if len(argv) < 2 :
    exit('usage ex : transition.py 771') 

if len(argv) == 2 :
    # Extract an array of heights from the string
    sequence = [ num(i) for i in argv[1] ]
    sequences = [sequence]
    print sequences[0]
    # exit if the siteswap isn't valid
    if not valid(sequence) :
        sequences = []
        print('Invalid siteswap sequence, you could try one of theses :')
        for p in permutations(sequence) :
            if valid(p) :
                #print(''.join([ str_(h) for h in p]))    
                sequences.append(p)

        #exit()

    # Now, let's get to work

    print str(sum(sequences[0])/len(sequences[0]))+' balls'
    for sequence in sequences :
        state = seq_state(sequence)
        entry = ground_state_to_seq_state(state)
        exit = seq_state_to_ground_state(state)

        print(str_(entry)+'('+str_(sequence)+')'+str_(exit))

if len(argv) == 3 :
    
    sequence1 = [ num(i) for i in argv[1] ]
    #print str_(sequence1)
    state1 = seq_state(sequence1)
    entry1 = ground_state_to_seq_state(state1)
    exit1 = seq_state_to_ground_state(state1)
    if VERBOSE : print state1
    
    sequence2 = [ num(i) for i in argv[2] ]
    #print str_(sequence2)
    state2 = seq_state(sequence2)
    entry2 = ground_state_to_seq_state(state2)
    exit2 = seq_state_to_ground_state(state2)
    if VERBOSE : print state2

    n = sum(sequence1)/len(sequence1)

    def match(a,b):
        for i,e in enumerate(a) :
            if not b[i] :
                if e :
                    return False
        return True

    def fill(a,b):
        if len(a) < len (b) :
            for i in range(len(b)-len(a)) :
                a.append(False)
        if len(b) < len (a) :
            for i in range(len(a)-len(b)) :
                b.append(False)

    l = len(state1)
    fill(state1,state2)
    matchable = []
    padding = 0
    for i in range(l):
        subset = state1[l-i:]
        if match(subset,state2):
            matchable = subset
            padding = l-i
    for i in range(len(state2)-len(matchable)) :
        matchable.append(False)
    if VERBOSE : print matchable
    if VERBOSE : print padding

    diff = [ i for i,a in enumerate(matchable) if a != state2[i] ]
    if VERBOSE : print diff
    
    transition = [ p+padding-i for i,p in enumerate(diff) ]
    
    print str_(entry1)+'('+str_(sequence1)+')'+str_(transition)+'('+str_(sequence2)+')'+str_(exit2)
    
    

