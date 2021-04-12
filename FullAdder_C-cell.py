def NOT(c):
    if c==0:
        c=1
    else:
        c=0
    return c
A=input("Enter 1st input bit:")
B=input("Enter 2nd input bit:")
c=int(input("Enter carry-in:"),2)
s0=int(A,2) | int(B,2)
s1=int(A,2) & int(B,2)
#print(s0)
#print(s1)
s=[]
s.append(s1)
s.append(s0)
#print(s)
s = ''.join(str(e) for e in s)
print(s)
if(s=="00" or s=="11"):
    sum1=c
    if(s=="00"):
        carry=0
    if(s=="11"):
        carry=1
if(s=="01" or s=="10"):
    sum1=NOT(c)
    carry=c
print("Sum Bit:",sum1)
print("Carry Bit:",carry)
