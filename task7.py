#Какое число является 10001-м простым числом?
array=[]
a=1
counter=0
while True:
    a+=1
    counter=0
    for i in range(2,a//2):
        if a%i==0:
            break
        else:
            counter+=1
    if counter==a//2-2:
        array.append(a)
    if len(array)==10000:
        break
print(array[-1])
