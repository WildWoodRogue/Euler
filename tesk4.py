array=[]
polylist=[]
number=0
breaker=0
for i in range(999,0,-1):
    for q in range(999,0,-1):
        number=q*i
        #print(q," ",i)
        array=list(str(number))
        if array==array[::-1]:
            polylist.append(int("".join(array)))
print(max(polylist))
