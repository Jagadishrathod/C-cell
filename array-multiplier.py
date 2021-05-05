A = int(input("Enter 1st input:"))
B = int(input("Enter 2nd input:"))
a=str(bin(A)[2:]) #binary conversion 
b=str(bin(B)[2:])
max_len = max(len(a), len(b))
n = max_len
print(max_len)
a= a.zfill(max_len)
b= b.zfill(max_len)
a1=[]
for i in range(len(a)):
    a1.append(a[i])
print(a1)
b1=[]
for i in range(len(b)):
    b1.append(b[i])
print(b1)

p = []
for i in range(len(b1)-1,-1,-1):
	for j in range(len(a1)-1,-1,-1):
		sum1 = int(a[j],2) & int(b[i],2)
		p.append(sum1)
#print(p)
for i in range(0, len(p), n):
	x = p[i:i+n]
	x.reverse()
	print(x)
result = 0
for i in range(len(b)):
	carry = 0
	inter_res = ""
	for j in range(len(a)-1,-1,-1):
		sum1 = int(b[j],2) * int(a[i],2) + carry
		if sum1 > 9 and j > 0:
			inter_res = str(sum1%10) + inter_res
			carry = sum1//10
		else:
			inter_res = str(sum1)+inter_res
			carry = 0
	result *= 10
	result += int(inter_res)
	print(result) ####################################
    