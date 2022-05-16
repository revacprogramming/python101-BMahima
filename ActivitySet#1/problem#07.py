# Strings
text = "X-DSPAM-Confidence:    0.8475"
search=text.find('0.8475')
s=text[search: ]
f=float(s)
print(f)
