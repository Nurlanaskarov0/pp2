#ex1
f = open("demofile.txt", "r")
print(f.read())

#ex2
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#ex3
f = open("demofile.txt", "r")
print(f.read(5))

#ex4
f = open("demofile.txt", "r")
print(f.readline())

#ex5
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#ex6
f = open("demofile.txt", "r")
for x in f:
  print(x)

#ex7
f = open("demofile.txt", "r")
print(f.readline())
f.close()