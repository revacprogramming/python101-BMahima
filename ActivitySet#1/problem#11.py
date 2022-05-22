# Tuples

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=0
d=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    s=line.split()
    y=s[5].split(':')
    z=y[0]
    d[z]=d.get(z,0)+1
for k,v in sorted(d.items()):
    print(k,v)
    