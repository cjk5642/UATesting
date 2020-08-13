import os

os.chdir('C:\\Users\\Connor\\Python Scripts\\')
#if working in windows must use double slashes

F = open('here.txt', 'r')
for x in F:
    print(os.system(str(x)))
