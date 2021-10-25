a=int(input("Введите число"))
b=0
while(a>0):
  d=a%10
  a=a//10
  b=b*10
  b=b+d
print(b)

