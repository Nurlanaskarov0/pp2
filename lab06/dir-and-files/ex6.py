import os
path =r'C:\Users\Нуртуган\Desktop\lab\lab06\dir-and-files'
if not os.path.exists(path):
    os.makedirs(path)

A = ord('A')
base = 'ex6.A-Z files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')