# Lists 

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

#lists  problem 8.5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    s=line.split()
    print(s[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")