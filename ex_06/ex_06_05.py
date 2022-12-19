str = 'X-DSPAM-Confidence:0.8475'
colon_str = str.find(":")
print(colon_str)
print(float(str[18+1:]))