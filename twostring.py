s1 = "abc"
s2 = "xyz"
result = ""

s2 = s2[::-1]

for i in range (len(s1)):
    result = result + s1[i] + s2[i]
print(result)
