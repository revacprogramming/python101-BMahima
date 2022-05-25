# Regular Expressions
# https://www.py4e.com/lessons/regex
filename=("dataset/regular_exp.txt")
handle=open(filename)
for line in handle:
    y=re.findall('[0-9]+',line)
    print(y)
  