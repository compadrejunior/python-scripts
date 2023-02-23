import os

# path to the folder
path = './data'

# iterate over all files in the folder
for filename in os.listdir(path):
    # open the file
    with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
        # read the lines in the file
        lines = f.readlines()
    # open the file for writing
    with open(os.path.join(path, filename), 'w', encoding='utf-8') as f:
        # iterate over all lines
        for line in lines:
            # if the line starts with banner::, replace it with an empty string
            if line.startswith('banner::'):
                line = ''
            # write the line
            f.write(line)
