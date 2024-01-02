a=int(input(' введите число'))
b=int(input(' введите число большее или равное, чем первое число'))
for i in range(a,b+1):
   if i % 2 == 0:
        print(i)
