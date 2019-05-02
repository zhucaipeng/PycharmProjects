f = open("/home/chrisz/a.txt","w")

'''
for I in f:
    print(I)
f.close()
'''

'''
print(f.readlines())
'''

f.write("first line\n")
f.write("second line\n")
f.close()

f = open("/home/chrisz/a.txt","r")
print(f.read())
f.close()