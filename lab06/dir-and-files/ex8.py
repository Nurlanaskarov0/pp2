import os 

path = r'C:\Users\Нуртуган\Desktop\lab\lab06\dir-and-files\ex8.txt'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.X_OK):
        print(f'File "{name}" can be eliminated')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be eliminated')
else:
    print(f'File "{name}" does\'t exist')