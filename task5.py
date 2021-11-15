#Какое самое маленькое число делится нацело на все числа от 1 до 20?
a=1
i=1
while True:

    if a%i==0:
        i+=1
    else:
        a+=1
        i=1
    if i==20:
        break
print(a)
