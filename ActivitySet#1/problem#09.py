# List
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    s=line.split()
    for i in s:
        if i in lst:
            continue
        else:
            lst.append(i)
    
lst.sort()
print(lst)
