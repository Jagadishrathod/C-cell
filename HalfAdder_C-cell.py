A=input("Enter 1st input bit:")
B=input("Enter 2nd input bit:")
s0=int(A,2) | int(B,2)
s1=int(A,2) & int(B,2)
s=[]
s.append(s0)
s.append(s1)
s = ''.join(str(e) for e in s)
print(s)
if(s=="00" or s=="11"):
    sum1=0
    if(s=="00"):
        carry=0
    if(s=="11"):
        carry=1
if(s=="01" or s=="10"):
    sum1=1
    if(s=="01"):
    	carry=0
    if(s=="10"):
    	carry=0
print("Sum Bit:",sum1)
print("Carry Bit:",carry)
