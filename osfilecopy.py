import os

source = input("Enter source file: ")
destination = input("Enter destination file: ")

src = os.open(source, os.O_RDONLY)

dest = os.open(destination,
               os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
               0o644)

data = os.read(src, 1024)

os.write(dest, data)

os.close(src)
os.close(dest)

print("File copied successfully.")
