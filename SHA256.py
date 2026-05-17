import hashlib

a=input("Enter first string: ")
b=input("Enter second string: ")

h1=hashlib.sha256(a.encode()).hexdigest()
h2=hashlib.sha256(b.encode()).hexdigest()

print("Hash1:",h1)
print("Hash2:",h2)

count=0

for i in range(len(h1)):
    if h1[i]!=h2[i]:
        count+=1

print("Different characters:",count)
