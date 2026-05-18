# View permissions
ls -l

# Create file and directory
touch file.txt
mkdir mydir

# Add permissions
chmod u+x file.txt
chmod g+w file.txt
chmod o+r file.txt

# Remove permissions
chmod u-x file.txt
chmod g-w file.txt
chmod o-r file.txt

# Full permissions
chmod a+rwx file.txt

# Exact symbolic permissions
chmod u=rwx,g=rx,o=r file.txt

# Numeric mode
chmod 777 file.txt
chmod 755 file.txt
chmod 644 file.txt

# Directory permissions
chmod 755 mydir
chmod 700 mydir

# Verify
ls -l file.txt
ls -ld mydir
