key = [[6,24,1],
       [13,16,10],
       [20,17,15]]

key_inv = [[8,5,10],
           [21,8,21],
           [21,12,8]]

text = input("Enter text: ").upper().replace(" ","")

# padding if length not multiple of 3
while len(text) % 3 != 0:
    text += "X"

cipher = ""

# Encryption
for i in range(0,len(text),3):
    a = ord(text[i]) - 65
    b = ord(text[i+1]) - 65
    c = ord(text[i+2]) - 65

    c1 = (key[0][0]*a + key[0][1]*b + key[0][2]*c) % 26
    c2 = (key[1][0]*a + key[1][1]*b + key[1][2]*c) % 26
    c3 = (key[2][0]*a + key[2][1]*b + key[2][2]*c) % 26

    cipher += chr(c1+65) + chr(c2+65) + chr(c3+65)

print("Encrypted:",cipher)


plain = ""

# Decryption
for i in range(0,len(cipher),3):
    a = ord(cipher[i]) - 65
    b = ord(cipher[i+1]) - 65
    c = ord(cipher[i+2]) - 65

    p1 = (key_inv[0][0]*a + key_inv[0][1]*b + key_inv[0][2]*c) % 26
    p2 = (key_inv[1][0]*a + key_inv[1][1]*b + key_inv[1][2]*c) % 26
    p3 = (key_inv[2][0]*a + key_inv[2][1]*b + key_inv[2][2]*c) % 26

    plain += chr(p1+65) + chr(p2+65) + chr(p3+65)

print("Decrypted:",plain)
