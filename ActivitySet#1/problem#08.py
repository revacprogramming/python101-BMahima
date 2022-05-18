# Files

fname = input("Enter file name: ")
fh = open(fname)
count=0
s=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    text=line.find('0.')
    t=line[text: ]
    f=float(t)
    s=s+f
    count=count+1
average=s/count
print("Average spam confidence:", average)

#files problem 8.4
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
