# count digits of a number
n=int(input("Enter a number:"))
n=str(n)
a=0
for i in n:
	a+=1
print("%s has %i digits"%(n,a))
