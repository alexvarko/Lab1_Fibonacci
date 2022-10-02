def fibonacci(n):
     if n in {0,1}:
         return n
     return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Введіть кількість чисел Фібоначі\n"))

if n <= 0:
   print("Число від'ємне, введіть додатнє число")
else:
   print("Числа Фібоначі:")
   for i in range(n):
       print(fibonacci(i), end=" ")