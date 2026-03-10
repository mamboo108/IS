key="MONARCHY"
alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"

s=""
for c in key+alpha:
    if c not in s:
        s+=c

m=[s[i:i+5] for i in range(0,25,5)]

def pos(x):
    for i in range(5):
        for j in range(5):
            if m[i][j]==x: return i,j

t=input("Text: ").upper().replace("J","I")
for i in range(0,len(t),2):
    a=t[i]; b=t[i+1] if i+1<len(t) else "X"
    r1,c1=pos(a); r2,c2=pos(b)

    if r1==r2: print(m[r1][(c1+1)%5]+m[r2][(c2+1)%5],end="")
    elif c1==c2: print(m[(r1+1)%5][c1]+m[(r2+1)%5][c2],end="")
    else: print(m[r1][c2]+m[r2][c1],end="")
