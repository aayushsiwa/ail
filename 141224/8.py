#max number in a list
n=int(input("Enter the numbers to enter in the array:"))
a=[]
max=0
for i in range(0,n):
	r=int(input("Enter element:"))
	if(i==0):
		max=r
	if(r>=max):
		max=r
print("Max is %i"%(max))
