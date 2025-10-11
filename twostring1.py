s = "abcdef"
even = ""
odd = ""
for i in range (len(s)):
    if i %2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]
        
print(even + odd)
