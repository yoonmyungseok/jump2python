f = open("C:/dev/study/python/jump2python/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()