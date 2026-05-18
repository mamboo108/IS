# List users
cat /etc/passwd | cut -d: -f1

# Add user
sudo adduser mec1

# Set password
sudo passwd mec1

# View passwd file
cat /etc/passwd

# Rename user
sudo usermod -l mec2 mec1

# Delete user
sudo userdel mec2
