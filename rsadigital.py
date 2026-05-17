from math import gcd

p=int(input("p: "))
q=int(input("q: "))

n=p*q
phi=(p-1)*(q-1)

e=int(input("e: "))

for d in range(1,phi):
    if (e*d)%phi==1:
        break

msg=input("Message: ")

m=sum(ord(i) for i in msg)

signature=(m**d)%n
print("Digital Signature:",signature)

verify=(signature**e)%n

if verify==m%n:
    print("Signature Verified")
else:
    print("Invalid Signature")
