text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(":")
new_text = text[ipos+4:]
parse = float(new_text)
print(parse)