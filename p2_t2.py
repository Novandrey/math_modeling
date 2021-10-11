a= int(input("Введите первый знаменатель"))
b= int(input("Введите знаменатель"))
c= int(input("Ведите количество членов прогрессии"))
d = [a*b**(n - 1)for n in range(1, c + 1)]
print(d)