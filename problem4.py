import os

# Specify the path to the directory
directory_path = '/Applications'

# Get the list of entries in the directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
