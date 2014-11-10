from sys import argv
from itertools import combinations

forbidden_in_multiplex = [0,1,2]

# Number of items
N = int(argv[1])
# Max height
H = int(argv[2])+1
# Period of the pattern
P = int(argv[3])

# String to describe the current state with multiplexes involved.
# init as the ground state
ground_state = '1'*N+'0'*(H-N)

# The current pattern being composed.
pattern = ''

def find_all(char, str):
    return [ i for i,v in enumerate([a for a in str]) if v == char]

# returns an array
def get_exits(state):
    ex = find_all('0',state)

    # enables multiplexing
    if not 2 in ex :
        ex.append(2)
        ex.sort()
    return ex

def insert(state,h):
    i = int(state[h])
    return state[0:h]+str(i+1)+state[h+1:]

def explore(state, pattern):
    if state == ground_state and pattern != '':
        print pattern
        return
    if len(pattern) >= P :
        return
    if state[0] == '0' :
        explore(state[1:], pattern+'0')
    if state[0] == '1' :
        ex = get_exits(state)
        for e in ex :
            # Make the throw
            s = insert(state, e)
            # advance in time
            s = s[1:]
            # fill with 0's
            s = s+'0'*(H-len(s))
            explore(s,pattern+str(e))
    if state[0] == '2' :
        ex = [ h for h in get_exits(state) if h not in forbidden_in_multiplex ]
        ex_ = combinations(ex,2)
        for e in ex_ :
            # Make the throws
            s = insert(state, e[0])
            s = insert(s, e[1])
            # advance in time
            s = s[1:]
            # fill with 0's
            s = s+'0'*(H-len(s))
            explore(s,pattern+'['+str(e[0])+str(e[1])+']')

explore(ground_state,'')
