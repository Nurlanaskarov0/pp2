import os
path =r'C:\Users\Нуртуган\Desktop\lab\lab06\dir-and-files'
if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')