#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
a=1
b=0
c=0
summ=0
while c<=4000000:
    c=a+b
    a=b
    b=c
    if c%2==0:
        summ+=c
print(summ)
