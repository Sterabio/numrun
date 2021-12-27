import time
import os
import random
import json




lenth = 30
back = 10

pos = 0

safe = [0 for i in range(back)] + [i for i in range(lenth)]

s = []
ns = []

n = 0
st = time.time()


def hs(name ,s,t):
    with open('hs.json','r') as f:
        hh = json.load(f)
    if name in dict(hh).keys():
        if hh[name]['score'] < s:
            hh[name]['score'] = s
            hh[name]['time'] = t
            print(f'new high score {hh[name]}')
            with open('hs.json','w') as f:
                json.dump(hh,f, indent=4)
            
        else:
            print(' - score:',s,'- high-score:', hh[name])
    else:
        hh[name] = {'score':s, 'time':t}
        print(f'new high score {hh[name]}')
        with open('hs.json','w') as f:
            json.dump(hh,f, indent=4)


tt = 0
name = input('Enter Name: ')
while True:
    
    
    os.system('cls||clear')
    pst = time.time()
    safe.extend([random.choice([i + pos + lenth - n,i + pos + lenth - n,0]) for i in range(n)])
    bb= 0
    for i in range(lenth):
        if i + pos in safe:
            s.append('_'* len(str(i + pos)) + ' ') 
            ns.append(str(i + pos) + ' ')
            bb +=1
        else:
            s.append('.'* len(str(i + pos)) + ' ')
            ns.append(' '* len(str(i + pos)) + ' ') 
    
    print(f'pos - {pos}')
    print(f'back - {back}')
    if back < 20:
        tback = back 
    else: 
        tback = 20
    print(str('  '*tback),f'pos - {pos}')
    print(str(' '*tback),f'back - {back}')
    
    print(str('  '*tback)+'()')
    print(str('`'*int(tback*2-1))+'[|\\')  
    print(str(' '*int(tback*2))+"/|")   
    print(str('  '*tback)+''.join(s[-lenth:]))
    print(str('. '*tback)+''.join(ns[-lenth:]))


    n = input()
    tt = round(time.time() - pst)
    if len(n) == 2:
        l = [i for i in n]
        n = int(l[0])* int(l[1])
    else:
        n = int(n)
    if pos+ n in safe:
        pass
    else:
        # os.system('clear')
        print(f'died jumping from {pos} to {pos +n} in {time.time()-st} seconds')
        
        hs(name,pos,time.time()-st)
        break
    
    back = int(back + n*len(str(pos))) - tt *3

    if back < 0:
        print(f'died taking too long jumping from {pos} to {pos +n} in {time.time()-st} seconds')
        hs(name,pos,tt)
        break
    
    pos= pos+ n
    

