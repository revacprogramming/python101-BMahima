# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    s=line.split()
    d[s[1]]=d.get(s[1],0)+1
bigd=None
bigword=None
for word,count in d.items():
    if bigd is None or count>bigd:
        bigword=word
        bigd=count
print(bigword,bigd)