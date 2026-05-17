from math import gcd

p=int(input("p: "))
q=int(input("q: "))

n=p*q
phi=(p-1)*(q-1)

e=int(input("e: "))

for d in range(1,phi):
    if (e*d)%phi==1:
        break

m=int(input("message: "))

c=(m**e)%n
print("Encrypted:",c)

m=(c**d)%n
print("Decrypted:",m)
