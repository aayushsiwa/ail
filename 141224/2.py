# wap to check if a string is pallindrome or not
a=str(input("Enter a string:"))
l=len(a)
#print(l)
mid=l//2
if l%2==0:
	for i in range(0,mid):
#		print(a[i])
#		print(a[-i-1])
		if a[i]==a[-i-1]:
			print("ok")
			continue
		else: 
			print("Not")
			break

else:
	for i in range(0,mid):
#		print(a[i])
#		print(a[-i-1])
		if a[i]==a[-i-1]:
			print("ok")
			continue
		else:
			print("not")
			break
