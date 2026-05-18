# Create file
touch my_test_file

# View ACL
getfacl my_test_file

# Add user permission
setfacl -m u:student:rw my_test_file

# Verify
getfacl my_test_file

# Add group permission
setfacl -m g:staff:r my_test_file

# Verify
getfacl my_test_file

# Remove user ACL
setfacl -x u:student my_test_file

# Verify
getfacl my_test_file

# Remove all ACLs
setfacl -b my_test_file

# Final verify
getfacl my_test_file
