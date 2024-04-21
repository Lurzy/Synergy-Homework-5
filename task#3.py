print("Введите минимальную сумму инвестиций:")
minInv = int(input())
print("Введите доступную сумму для инвестиции у Ивана:")
invIvan = int(input())
print("Введите доступную сумму для инвестиции у Майкла:")
invMike = int(input())

sumInv = invIvan + invMike
print("Общая сумма инвестиций: ", sumInv)

if (invIvan >= minInv) and (invMike >= minInv):
    print("2")
elif (invIvan >= minInv) and (invMike <= minInv):
    print("Ivan")
elif (invIvan <= minInv) and (invMike >= minInv):
    print("Mike")
elif sumInv >= minInv:
    print("1")
else: 
    print("0")