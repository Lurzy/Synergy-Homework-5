print("Введите слово из латинских букв: ")
userWord = input().lower()

#Задаю каждой гласной буве переменную, которая будет считать из userWord их количество
letA = userWord.count('a')
letE = userWord.count('e')
letI = userWord.count('i')
letO = userWord.count('o')
letU = userWord.count('u')

#Считаю сумму гласных
vowelsCounts = letA + letE + letI + letO + letU
print("Согласных  букв в слове: ", vowelsCounts)

#Задаю переменную для согласных букв и высчитываю ее. Беру всю длину слова и вычитаю ранее посчитанные гласные буквы
consonants = len(userWord) - vowelsCounts
print("Согласных букв в слове: ", consonants)

#Вывод количества гласных букв в слове
if letA == 0:
    print("Количество согласных букв 'A': False")
else: 
    print("Количество согласных букв 'A': ", letA )

if letE == 0:
    print("Количество согласных букв 'E': False")
else: 
    print("Количество согласных букв 'E': ", letE )

if letI == 0:
    print("Количество согласных букв 'I': False")
else: 
    print("Количество согласных букв 'I': ", letI )

if letO == 0:
    print("Количество согласных букв 'O': False")
else: 
    print("Количество согласных букв 'O': ", letO )

if letU == 0:
    print("Количество согласных букв 'U': False")
else: 
    print("Количество согласных букв 'U': ", letU )
    