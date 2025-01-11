#nth fibonacci number
n=int(input("Enter the number:"))
x=0
y=1
for i in range(n):
	z=x+y
	x=y
	y=z

print(x)
