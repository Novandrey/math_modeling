a=float(input("Введите первое число"))
b=float(input("Введите второе число"))
c=float(input("Введите третье число"))
if(a+b<c or b+c<a or a+c<b):
  print("Такого треугольника  не существует")
elif(a==b and a==c):
  print("Равносторонний")
elif(a==b or a==c or b==c):
  print("равнобедренный")
else:
  print("Разносторонний")
