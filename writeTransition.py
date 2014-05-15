from sys import argv
from itertools import permutations

VERBOSE = False

# str -> array of ints
def num(i):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    val = alphabet.find(i)
    if val == -1 :
        exit_('Not supported : %s, allowed : [0123456789abcdefghijklmnopqrstuvwxyz]'%i)
    return(val)

# array of ints -> str
def str_(a):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    return(''.join([ alphabet[i] for i in a ]))

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
    entrance = []
    for i in state :
        if i :
            entrance.append(n+e)
        else :
            e += 1
    while entrance[0] == n :
        if len(entrance) == 1 :
            #exit_('When I say excited, I mean excited. Asshole !')
            return([])
        entrance = entrance[1:]
    return(entrance)

# determine the transition to enter the ground state from the state of the sequence
def seq_state_to_ground_state(state):
    exit_ = []
    while len([ p for p in state if not p ]) > 0 :
        h = state.index(False)
        exit_.append(h)
        set_taken(h,state)
        state = state[1:]
    return(exit_)

def excitment(state):
    return ''.join([ str(int(i)) for i in state[::-1]])




sequences = file(argv[1]).readlines()




output = open('out_tran','w')

current = 0
#print str(sum(sequences[0])/len(sequences[0]))+' balls'
for sequence in sequences :
    sequence = [ num(i) for i in sequence[:-1] ]
    state = seq_state(sequence)
    exci = excitment(state).zfill(30)
    entrance = ground_state_to_seq_state(state)
    # not excited
    if entrance == []:
        output.write(exci+' '+str_(sequence)+'\n')
        current += 1
    else :
        exit_ = seq_state_to_ground_state(state)
        ent = str_(entrance)
        seq = str_(sequence)
        exi = str_(exit_)
        output.write(exci+' '+ent+'('+seq+')'+exi+'\n')
        current += 1

    if current%5000 == 0 :
        print 'Transitions calculated : '+str(current)

print  'Transitions calculated : '+str(current)
