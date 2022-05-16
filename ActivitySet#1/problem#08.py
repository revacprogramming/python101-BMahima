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

