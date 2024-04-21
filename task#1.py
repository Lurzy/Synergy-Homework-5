print("Введите число")
userNumber = int(input())

if userNumber == 0:
    print("Это нулевое число")
elif userNumber > 0:
    if userNumber % 2 == 0:
        print("Это положительно четное число")
    else: 
        print("Это положительное нечетное число")
else: 
    if userNumber % 2 == 0:
        print("Это отрицательно четное число")
    else:
        print("Это отрицательное нечетное число")