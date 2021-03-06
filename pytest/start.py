print("Xavi")
f = open("test.txt",'r')
lines = f.readlines()
for line in lines: 
    print("{}".format(line.strip()))
