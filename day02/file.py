import sys

#f = open("/home/chrisz/a.txt","r")



with open("/home/chrisz/a.txt","r") as f:
    print(f.readlines())

'''
for I in f.readlines():
    print(I)
f.close()
'''

'''
f.write("first line\n")
f.write("second line\n")
f.close()

f = open("/home/chrisz/a.txt","r")
print(f.read())
f.close()
'''