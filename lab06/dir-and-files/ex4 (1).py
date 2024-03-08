import os
path = r'C:\Users\Нуртуган\Desktop\lab\lab06\dir-and-files'

files = os.listdir(path)
with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.base_name(path), len(lines)))