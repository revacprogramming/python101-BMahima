# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
filename=("regg.txt")
handle=open(filename)
sum=0
lst=list()
for line in handle:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    lst=lst+y
for i in lst:
    sum=sum+int(i)
print(sum)


'''import re
filename=("regg.txt")
handle=open(filename).read()
sum=0
y=re.findall('[0-9]+',handle)
for i in y:
  sum=sum+int(i)
print(sum)'''
    

    

  #if len(y)!=1: continue