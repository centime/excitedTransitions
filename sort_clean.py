from sys import argv 

output = open('cleaned','w')
sequences = file(argv[1]).readlines()

exciteds = []
bases = []
for seq in sequences :
    if '(' in seq :
        [state, e] = seq.split(' ')
        [ent, main, ex] = e.replace(')','(').split('(')
        if main[0]!= '0':
            exciteds.append(state+' '+ent+'('+main.zfill(20)+')'+ex)
    else :
        bases.append(seq[:-1].split(' ')[1].zfill(20))

bases.sort()

met = set([])

current = 0
for s in bases   :
    s = s.lstrip('0')
    write = True
    for i in range(len(s)):
        ii = i+1
        pre = s[:ii] 
        post = s[-ii:]
        if pre in met or post in met :
            write = False
            break
    if write :
        output.write(s+'\n')
        met.add(s)
        current += 1
    if current % 5000 == 0:
        print current
    

exciteds.sort()
# for i in exciteds :
#     print i

excitments = {}

for e in exciteds :
    [ex_state, e] = e.split(' ')
    [ent, seq, ex] = e.replace(')','(').split('(')
    seq = seq.lstrip('0')
    
    if not(ex_state in excitments) :
        excitments[ex_state] = set([])
     

    l = len(seq)
    write  = True

    #remove it if it is a combination of known patterns
    if write :
        for i in range(l):
            ii = i+1
            pre = seq[:ii] 
            post = seq[-ii:]
            if pre in met or post in excitments[ex_state] :
                if seq == '915' :
                    print 'here'

                write = False
                break
    #remove it if ent+start is a known pattern
    #ex : 6(456)4
    if write :
        for i in range(l-len(ent)):
            ii = i+1
            pre = seq[:ii]
            if ent+pre in met :
                write = False
                break

    #remove if the excited pattern is a rotation of an already knonw one
    if write :
        for i in range(l):
            s = seq[-(l-i):]+seq[:i]
            if s in met :
                write = False
                break

    if write :
        output.write(ent+'('+seq+')'+ex)
        met.add(seq)
        excitments[ex_state].add(seq)    
        current += 1

    if current % 5000 == 0:
        'Selected after clean-up : '+str(current)
print 'Selected after clean-up : '+str(current)
