#ex1
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#ex2
f = open("myfile.txt", "x")

#ex3
f = open("myfile.txt", "w")
