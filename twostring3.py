s = "python"
result = ""
for i in range (0, len(s), 2):
    if i + 1 < len(s):
        result = result + s[i + 1] + s[i]
    else:
        result = result + s[i]
print(result)