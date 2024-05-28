a = int(input())

b = a//200
c = (a-(b*200))//100
d = (a-(b*200)-(c*100))//50

n = c+(b*3)+1

print(n)