f=open('zero_one.txt')
for line in f:
    if int(line)==0:
        line='1'
    else:
        line='0'

print("New grid:",line)

f.close() 
